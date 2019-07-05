//
// Created by maryana on 18.03.18.
//
#include <iostream>
#include <fstream>
#include <limits>
#include <chrono>
#include <cassert>
#include <atomic>
#include <cmath>
#include <map>
#include <vector>
#include <thread>
using namespace std;


inline std::chrono::steady_clock::time_point get_current_time_fenced() {
    assert(std::chrono::steady_clock::is_steady &&
           "Timer should be steady (monotonic).");
    std::atomic_thread_fence(std::memory_order_seq_cst);
    auto res_time = std::chrono::steady_clock::now();
    std::atomic_thread_fence(std::memory_order_seq_cst);
    return res_time;
}


template<class D>
inline long long to_us(const D& d) {
    return std::chrono::duration_cast<std::chrono::microseconds>(d).count();
}


double func_to_integrate(const double& x1, const double& x2) {
    int c [5] = {2,1,4,7,2};
    int a1 [5] = {1,2,1,1,5};
    int a2 [5] = {4,5,1,2,4};
    double f = 0.0;
    for (int i = 0; i <= 4; ++i) {
        f += c[i] * exp(-1/M_PI * ( (x1-a1[i])*(x1-a1[i]) + (x2-a2[i])*(x2-a2[i]) )) * cos(M_PI * ( (x1-a1[i])*(x1-a1[i]) + (x2-a2[i])*(x2-a2[i]) ));
    }
    return -f;
}


void integrate( double a, double b, double c, double d, int steps_x, int steps_y, double& res) {
    double dx = (b-a)/steps_x;
    double dy = (d-c)/steps_y;
    double xi = a;
    double V = 0;

    for (int i = 1; i <= steps_x; ++i)
    {
        double yi = c;
        for (int j = 1; j <= steps_y; ++j)
        {
            double fij = func_to_integrate(xi + dx/2, yi + dy/2);
            V += fij*dx*dy;
            yi += dy;
        }
        xi += dx;
    }
    res = V;
}


double parallelize_intgr(pair<double, double> x_intrv, pair<double, double> y_intrv,
                         int steps_x, int steps_y, int num_thr){
    vector<thread> threads;
    double *integrals;
    integrals = new double [num_thr];

    double start = y_intrv.first;
    double thread_step = (y_intrv.second-y_intrv.first)/num_thr;
    double end = y_intrv.first + thread_step;
    for (int i = 0; i < num_thr; ++i) {
        threads.emplace_back(integrate, x_intrv.first, x_intrv.second, start,
                             end, steps_x, steps_y, ref(integrals[i]));
        start += thread_step;
        end += thread_step;
    }
    for (int k = 0; k < num_thr; ++k) { threads[k].join(); }

    double total_volume = 0;
    for (int j = 0; j < num_thr; ++j) {
        total_volume += integrals[j];
    }
    return total_volume;
}


int main(int argc, char **argv) {

    if (argc < 9 ){
        cerr << "There must be 9 arguments \n usage: <abs err> <rel err> <steps_x> <steps_y> <num of threads>"
                " <x_intrv lower> <x_intrv upper> <y_intrv lower> <y_intrv upper>" << endl;
        return 1;
    }
    if (atof(argv[6]) > atof(argv[7]) || atof(argv[8]) > atof(argv[9])){
        cerr << "Wrong interval: upper bound is less than lower \n usage: <abs err> <rel err> <steps_x> <steps_y> "
                "<num of threads> <x_intrv lower> <x_intrv upper> <y_intrv lower> <y_intrv upper>" << endl;
        return 1;
    }
    if (atof(argv[1])>1.0){
        cerr << "absolute error can not be > 1 \n usage: <abs err> <rel err> <steps_x> <steps_y> "
                "<num of threads> <x_intrv lower> <x_intrv upper> <y_intrv lower> <y_intrv upper>" << endl;
        return 1;
    }
    if (atof(argv[2])>1.0){
        cerr << "relative error can not be > 1 \n usage: <abs err> <rel err> <steps_x> <steps_y> "
                "<num of threads> <x_intrv lower> <x_intrv upper> <y_intrv lower> <y_intrv upper>" << endl;
        return 1;
    }

    double abs_err = atof(argv[1]);
    double rel_err = atof(argv[2]);
    int steps_x = atoi(argv[3]);
    int steps_y = atoi(argv[4]);
    int num_thr = atoi(argv[5]);
    pair <double, double> x_intrv (atof(argv[6]), atof(argv[7]));
    pair <double, double> y_intrv (atof(argv[8]), atof(argv[9]));

//    double abs_err = 0.001;
//    double rel_err = 0.001;
//    int steps_x = 809;
//    int steps_y = 809;
//    int num_thr = 29;
//    pair <double, double> x_intrv (-10.0, 10.0);
//    pair <double, double> y_intrv (-10.0, 10.0);

    double max_steps = 3000;
    int x_steps_in_thr = steps_x/num_thr;
    int y_steps_in_thr = steps_y/num_thr;

    auto before = get_current_time_fenced();

    double cur_res = parallelize_intgr(x_intrv, y_intrv, x_steps_in_thr, y_steps_in_thr, num_thr);

    double prev_res = cur_res;
    bool to_continue = true;
    double cur_abs_err = -1;
    double cur_rel_err = -1;

    while( to_continue )
    {
        x_steps_in_thr *= 2;
        y_steps_in_thr *= 2;
        cur_res = parallelize_intgr(x_intrv, y_intrv, x_steps_in_thr, y_steps_in_thr, num_thr);
        cur_abs_err = fabs(cur_res-prev_res);
        cur_rel_err = fabs( (cur_res-prev_res)/cur_res );

        to_continue = ( cur_abs_err > abs_err );
        to_continue = to_continue && ( cur_rel_err > rel_err );
        to_continue = to_continue && (x_steps_in_thr*num_thr < max_steps && y_steps_in_thr*num_thr < max_steps);
        prev_res = cur_res;

    }

    auto time_to_calculate = to_us(get_current_time_fenced() - before);

    cout << cur_res << " " << time_to_calculate  << endl;
    cout << "Abs err : rel err " << cur_abs_err << " : " << cur_rel_err << endl;
    return 0;
}