#include <assert.h>
#include <iostream>
#include <fstream>


unsigned hammingDistance(std::string dna1, std::string dna2){

    assert(dna1.length() == dna2.length());
    unsigned distance = 0;
    for(auto x=0; x<dna1.length(); x++){
        if(dna1.at(x) != dna2.at(x)){
            distance++;
        }
    }
    return distance;
}


int main(void){

    std::ifstream input("rosalind_hamm.txt");
    std::string dnaString1;
    std::string dnaString2;
    std::getline(input, dnaString1);
    std::getline(input, dnaString2);
    std::cout << "Initial strings:" << std::endl;
    std::cout << dnaString1 << std::endl;
    std::cout << dnaString2 << std::endl;

    std::cout << "Hamming distance:" << std::endl;
    std::cout << hammingDistance(dnaString1, dnaString2) << std::endl;
    return 0;
}
