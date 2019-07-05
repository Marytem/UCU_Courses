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


int count_happy(int start, long end, int digit_num){
    int happy_sum = 0;
    for (int ticket = start; ticket <= end; ++ticket) {
        int left = (ticket/power(10,digit_num/2));
        int right = ticket % power(10,digit_num/2);

        if (digit_sum(left) == digit_sum(right)) {
            happy_sum++;
        }
    }
    return happy_sum;
}


int main() {
    int total_happy = 0;


    auto start_normal = get_current_time_fenced();

    total_happy = count_happy(0, 9999999999, 10);

    auto end_normal = get_current_time_fenced();


    auto res_normal = to_us(end_normal - start_normal);

    std::cout << res_normal << std::endl;
    std::cout << total_happy << std::endl;
    return 0;
}
