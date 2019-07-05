all: parallel normal

normal: normal.o
	g++ -pthread normal.o -o normal

parallel: parallel.o
	g++ -pthread parallel.o -o parallel

parallel.o: parallel.cpp
	g++ -c -std=c++14 -Og parallel.cpp -o parallel.o

normal.o: normal.cpp
	g++ -c -std=c++14 -Og normal.cpp -o normal.o
