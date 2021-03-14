#include <iostream>
#include <fstream>
#include <map>

std::map<char, double> massTable = {{'A', 71.03711},
                                    {'C', 103.00919},
                                    {'D', 115.02694},
                                    {'E', 129.04259},
                                    {'F', 147.06841},
                                    {'G', 57.02146},
                                    {'H', 137.05891},
                                    {'I', 113.08406},
                                    {'K', 128.09496},
                                    {'L', 113.08406},
                                    {'M', 131.04049},
                                    {'N', 114.04293},
                                    {'P', 97.05276},
                                    {'Q', 128.05858},
                                    {'R', 156.10111},
                                    {'S', 87.03203},
                                    {'T', 101.04768},
                                    {'V', 99.06841},
                                    {'W', 186.07931},
                                    {'Y', 163.06333}};


double calculateProteinMass(std::string proteinString){

    double totalMass = 0.0;
    for(auto it=proteinString.begin(); it!=proteinString.end(); ++it){
        totalMass += massTable[*it];
        // std::cout << totalMass << std::endl;
    }
    return totalMass;
}


int main(void){

    std::ifstream input("rosalind_prtm.txt");
    std::string proteinString;
    std::getline(input, proteinString);
    std::cout << "Initial string:" << std::endl;
    std::cout << proteinString << std::endl;
    std::cout.unsetf(std::ios::floatfield);
    std::cout.precision(9);
    double totalMass = calculateProteinMass(proteinString);
    std::cout << totalMass << std::endl;
    return 0;
}
