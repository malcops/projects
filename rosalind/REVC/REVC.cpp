#include <algorithm>
#include <iostream>
#include <fstream>
#include <map>


std::string complementDNA(std::string dnaString){

    std::string complement;
    std::map<char, char> complements = {{'A', 'T'}, {'C', 'G'}, {'G', 'C'}, {'T', 'A'}};
    for(auto it=dnaString.begin(); it!=dnaString.end(); ++it){
        complement += complements[*it];
    }
    return complement;
}


std::string reverseDNA(std::string dnaString){

    std::string copy(dnaString);
    std::reverse(copy.begin(), copy.end());
    return copy;
}


int main(void){

    std::ifstream input("rosalind_revc.txt");
    std::string dnaString;
    std::getline(input, dnaString);
    std::cout << "Initial string:" << std::endl;
    std::cout << dnaString << std::endl;

    auto complementString = complementDNA(dnaString);
    std::cout << "Complement string:" << std::endl;
    std::cout << complementString << std::endl;
    auto finalString = reverseDNA(complementString);
    std::cout << "Final string:" << std::endl;
    std::cout << finalString << std::endl;

    return 0;
}
