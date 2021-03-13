#include <assert.h>
#include <iostream>
#include <fstream>
#include <map>


std::string translateRNA(std::string rnaString){

    const int CODON_LENGTH=3;
    assert(rnaString.length() % CODON_LENGTH == 0);
    const std::map<std::string, std::string> rnaCodonTable { {"UUU", "F"}, {"CUU", "L"}, {"AUU", "I"}, {"GUU", "V"},
                                                             {"UUC", "F"}, {"CUC", "L"}, {"AUC", "I"}, {"GUC", "V"},
                                                             {"UUA", "L"}, {"CUA", "L"}, {"AUA", "I"}, {"GUA", "V"},
                                                             {"UUG", "L"}, {"CUG", "L"}, {"AUG", "M"}, {"GUG", "V"},
                                                             {"UCU", "S"}, {"CCU", "P"}, {"ACU", "T"}, {"GCU", "A"},
                                                             {"UCC", "S"}, {"CCC", "P"}, {"ACC", "T"}, {"GCC", "A"},
                                                             {"UCA", "S"}, {"CCA", "P"}, {"ACA", "T"}, {"GCA", "A"},
                                                             {"UCG", "S"}, {"CCG", "P"}, {"ACG", "T"}, {"GCG", "A"},
                                                             {"UAU", "Y"}, {"CAU", "H"}, {"AAU", "N"}, {"GAU", "D"},
                                                             {"UAC", "Y"}, {"CAC", "H"}, {"AAC", "N"}, {"GAC", "D"},
                                                             {"UAA", "" }, {"CAA", "Q"}, {"AAA", "K"}, {"GAA", "E"},
                                                             {"UAG", "" }, {"CAG", "Q"}, {"AAG", "K"}, {"GAG", "E"},
                                                             {"UGU", "C"}, {"CGU", "R"}, {"AGU", "S"}, {"GGU", "G"},
                                                             {"UGC", "C"}, {"CGC", "R"}, {"AGC", "S"}, {"GGC", "G"},
                                                             {"UGA", "" }, {"CGA", "R"}, {"AGA", "R"}, {"GGA", "G"},
                                                             {"UGG", "W"}, {"CGG", "R"}, {"AGG", "R"}, {"GGG", "G"} };

    std::string proteinString;
    for(auto idx=0; idx<rnaString.length(); idx=idx+CODON_LENGTH){
        std::string codon = rnaString.substr(idx, CODON_LENGTH);
        std::string aminoAcid = rnaCodonTable.at(codon);
        proteinString += aminoAcid;
    }

    return proteinString;
}


int main(void){

    std::ifstream input("rosalind_prot.txt");
    std::string rnaString;
    std::getline(input, rnaString);
    std::cout << "RNA input:" << std::endl;
    std::cout << rnaString << std::endl;

    std::string proteinString = translateRNA(rnaString);
    std::cout << "Protein output:" << std::endl;
    std::cout << proteinString << std::endl;
    return 0;
}
