CXX = g++
FLAGS = -std=c++20 -O2 -Wall -Wextra
TARGET = main

all:$(TARGET)

main:
	$(CXX) $(FLAGS) "BEE 1169.cpp" -o $(TARGET)

test:
	main.exe < input.txt

testp:
	python "BEE 1169.py" < input.txt

clean:
	if exist main.exe del main.exe