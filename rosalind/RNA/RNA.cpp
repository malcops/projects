#include <algorithm>
#include <iostream>
#include <fstream>


std::string transcribeDNA(std::string dnaString){

    std::replace(dnaString.begin(), dnaString.end(), 'T', 'U');
    return dnaString;
}


int main(void){

    std::ifstream input("rosalind_rna.txt");
    std::string dnaString;
    std::getline(input, dnaString);
    std::cout << "Initial string:" << std::endl;
    std::cout << dnaString << std::endl;

    auto rnaString = transcribeDNA(dnaString);
    std::cout << "Final string:" << std::endl;
    std::cout << rnaString << std::endl;
    return 0;
}
