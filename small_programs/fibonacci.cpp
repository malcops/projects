// Calculates the Nth value in the Fibonacci sequence
#include <iostream>
#include <assert.h>

void fibonacci(unsigned terms[3]){

    unsigned temp = terms[1] + terms[2];
    terms[0] = terms[1];
    terms[1] = terms[2];
    terms[2] = temp;

    return;
}

int main(int argc, char *argv[]){

    assert(argv[1]);
    std::cout << "Term " << argv[1] << " was requested:" << std::endl;
    unsigned maxCount = atoi(argv[1]);

    // term 2
    unsigned count = 3;
    unsigned array[3] = {1, 1, 2};

    while(count <= maxCount){
        std::cout << "array: " << array[0] << " " << array[1] << " " << array[2] << std::endl;
        std::cout << "count: " << count << " term: " << array[2] << std::endl;
        fibonacci(array);
        count++;
    }
}

