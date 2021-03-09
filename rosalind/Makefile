CXX=g++
GTEST_FLAGS=-lgtest -lpthread

.PHONY: test dna

all: test dna

test:
	$(CXX) DNA.cpp  -o gtest

dna:
	$(CXX) DNA/DNA.cpp -o DNA/dna
