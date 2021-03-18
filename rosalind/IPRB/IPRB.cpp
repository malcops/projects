#include <iostream>
#include <fstream>


float calculation(int k, int m, int n){

    int total = k + m + n;
    float kChosen = float(k)/total;
    float mChosen = float(m)/total;
    float nChosen = float(n)/total;
    std::cout << kChosen << std::endl;

    float kDominant = float(1);
    float mDominant = float(1)/2;
    float nDominant = float(0);

    std::cout << mDominant << std::endl;

}


int main(void){

    std::ifstream input("rosalind_iprb.txt");
    std::string inputString;
    std::getline(input, inputString,' ');
    int k = std::stoi(inputString);
    std::getline(input, inputString,' ');
    int m = std::stoi(inputString);
    std::getline(input, inputString);
    int n = std::stoi(inputString);
    std::cout << k << " " << m << " " << n << std::endl;
    // k = homozygous dominant  XX
    // m = heterozygous         Xx
    // n = homozygous recessive xx

    // calculate % an offspring will have at least 1 dominant allele (X)
    calculation(k, m, n);

    return 0;
}
