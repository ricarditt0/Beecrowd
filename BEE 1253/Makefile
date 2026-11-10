CXX = g++
FLAGS = -std=c++20 -O2 -Wall -Wextra
TARGET = main

all:$(TARGET)

main:
	$(CXX) $(FLAGS) "BEE 1253.cpp" -o $(TARGET)

clean:
	if exits main.exe del main.exe

test:
	main.exe < input.txt

.PHONY: all clean
