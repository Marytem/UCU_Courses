#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <thread>
#include <algorithm>
#include <cassert>
#include <atomic>


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



struct config{
    string inp_f;
    string al_out;
    string num_out;
    int num_thr;
    config(){}
    config(vector<string> con_vec){
        inp_f = con_vec[0];
        al_out = con_vec[1];
        num_out = con_vec[2];
        num_thr = atoi(con_vec[3].c_str());
    }
};


vector<string> read_file(const string& filename){
    ifstream inp_fs;
    inp_fs.open(filename, ifstream::in);
    vector<string> words;
    string tmp;
    while (inp_fs >> tmp) {
        words.push_back(move(tmp));
    }
    inp_fs.close();
    return words;
}


void count_words(const vector<string>& words, const int start, const int end,
                 map<string, int>& res_dict){
    for (int i = start; i < end; ++i) {
        res_dict[words[i]] ++;
    }
};


int main(int argc, char **argv) {
    //reading configs
    config conf;
    string confname = "config";
    try{
        if (argc > 1){confname = (argv[1]);}
        conf = config(read_file(confname));
    }
    catch (exception& ex){cerr << "No configuration file in current directory";}

    //reading words in vector
    auto start_reading = get_current_time_fenced();
    vector<string> words = read_file(conf.inp_f);
    auto words_size = words.size()-1;
    map<string, int> dicts [conf.num_thr];
    auto reading_time = to_us(get_current_time_fenced() - start_reading);


    //parallelizing itself: making num_thr dicts
    vector<thread> threads;
    auto thr_step = words.size()/conf.num_thr;
    auto start = 0;
    auto end = thr_step;

    auto start_counting = get_current_time_fenced();
    for (int i = 0; i < conf.num_thr-1; ++i) {
        threads.emplace_back(count_words, ref(words), start, end, ref(dicts[i]));
        start += thr_step;
        end += thr_step;
    }
    threads.emplace_back(count_words, ref(words), start, words.size(), ref(dicts[conf.num_thr-1]));
    for (int k = 0; k < conf.num_thr; ++k) { threads[k].join(); }
    auto counting_time = to_us(get_current_time_fenced() - start_counting);


    //merging them
    map<string, int> merged_map;
    for (auto& dict : dicts){
        for (auto& w_pair : dict){
            merged_map[w_pair.first] += w_pair.second;
        }
    }

    // making vector for further sorting while writing existing alphabetic result
    vector<pair<string, int>> vector_map;
    ofstream out_fs;
    out_fs.open(conf.al_out);
    for (auto& w_pair : merged_map){
        vector_map.emplace_back(w_pair);
        out_fs << w_pair.first + " : " + to_string(w_pair.second) + "\n";
    }
    out_fs << "\0";
    out_fs.close();

    //sorting and printing numeric result
    sort(vector_map.begin(), vector_map.end(), [](pair<string, int> pair1, pair<string, int> pair2)
            -> bool{ return pair1.second < pair2.second;});
    out_fs.open(conf.num_out);
    for (auto& w_pair : vector_map){
        out_fs << w_pair.first + " : " + to_string(w_pair.second) + "\n";
    }
    out_fs << "\0";
    out_fs.close();

    auto total_time = to_us(get_current_time_fenced() - start_reading);

    cout << "reading: " << reading_time << endl;
    cout << "counting: " << counting_time << endl;
    cout << "total: " << total_time << endl;
    return 0;
}