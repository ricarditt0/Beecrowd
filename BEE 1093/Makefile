CXX = g++
FLAGS = -std=c++20 -O2 -Wall -Wextra
TARGET = main

all:$(TARGET)

main:
	$(CXX) $(FLAGS) "BEE 1093.cpp" -o $(TARGET)

test:
	main.exe < input.txt

clean:
	if exist main.exe del main.exe