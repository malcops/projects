#include<iostream>
#include <fstream>
#include <map>


std::map<char, unsigned> countBases(std::string nucleotide){

    std::map<char, unsigned> counts = {{'A', 0}, {'C', 0}, {'G', 0}, {'T', 0}};
    for(auto it=nucleotide.begin(); it != nucleotide.end(); ++it){
        counts[*it]++;
    }
    return counts;
}


int main(void){

    std::ifstream input("rosalind_dna.txt");
    std::string sequence;
    std::getline(input, sequence);
    std::cout << sequence << std::endl;
    std::cout << sequence.length() << std::endl;

    auto counts = countBases(sequence);
    char buffer[100];
    sprintf(buffer, "%d %d %d %d", counts['A'], counts['C'], counts['G'], counts['T']);
    std::cout << buffer << std::endl;
    return 0;
}
