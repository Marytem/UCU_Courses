#include <iostream>
#include <chrono>
#include <atomic>
#include <thread>
using namespace std;


inline std::chrono::high_resolution_clock::time_point get_current_time_fenced()
{
    std::atomic_thread_fence(std::memory_order_seq_cst);
    auto res_time = std::chrono::high_resolution_clock::now();
    std::atomic_thread_fence(std::memory_order_seq_cst);
    return res_time;
}


template<class D>
inline long long to_us(const D& d)
{
    return std::chrono::duration_cast<std::chrono::microseconds>(d).count();
}


inline int digit_sum(int num){
    int digit,sum = 0;
    while(num>0)
    {
        digit = num % 10;
        num /= 10;
        sum += digit;
    }
    return sum;
}


inline int power(int bas, int expon){
    int res = 1;
    for (int i = 0; i < expon ; ++i) {
        res *= bas;
    }
        return res;
}


void count_happy_parallel(int start, long end, int digit_num, int& res){
    int happy_sum = 0;
    for (int ticket = start; ticket <= end; ++ticket) {
        int left = (ticket/power(10,digit_num/2));

        int right = ticket % power(10,digit_num/2);
        if (digit_sum(left) == digit_sum(right)) {
            happy_sum++;
        }
    }
    res = happy_sum;
}


int main(int argc, char **argv) {
    int num_thr = atoi(argv[1]);
//    int num_thr = 1000;
    int start = 0;
    int digit_num = 10;
    int step = (power(10, digit_num)-1)/num_thr;
    int end = step;

    thread **threads;
    threads = new thread* [num_thr];

    int * sums;
    sums = new int [num_thr];


    auto start_parallel = get_current_time_fenced();

    for (int i = 0; i < num_thr; ++i) {
        threads[i] = new thread(count_happy_parallel, start, end, digit_num, ref(sums[i]));
        start += step+1;
        end += step+1;
    }

    for (int k = 0; k < num_thr; ++k) { threads[k]->join(); }

    int total_happy = 0;
    for (int j = 0; j < num_thr; ++j) { total_happy += sums[j]; }

    auto end_parallel = get_current_time_fenced();


    auto res_parallel = to_us(end_parallel - start_parallel);
    std::cout << res_parallel << std::endl;
    std::cout << total_happy << std::endl;
    return 0;
}