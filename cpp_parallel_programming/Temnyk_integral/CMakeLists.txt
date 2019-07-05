cmake_minimum_required(VERSION 3.9)
project(integral)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -pthread")

add_executable(integral linear_int.cpp)