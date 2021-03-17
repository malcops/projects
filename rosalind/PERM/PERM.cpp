#include <algorithm>
#include <assert.h>
#include <iostream>
#include <fstream>
#include <numeric>
#include <vector>


int main(void){

    std::ifstream input("rosalind_perm.txt");
    std::string inputString;
    std::getline(input, inputString);
    int n = std::stoi(inputString);
    assert(n<=7);

    std::vector<int> v(n);
    std::iota (v.begin(), v.end(), 1);

    // total permutations
    int factorial = 1;
    for(auto it=v.begin();it!=v.end();++it){
        factorial *= *it;
    }
    std::cout << factorial << std::endl;

    // output each permutation
    do{
        for(auto it=v.begin();it!=v.end();++it){
            std::cout << *it << " ";
        }
        std::cout << std::endl;
    } while(std::next_permutation(v.begin(),v.end()));

    return 0;
}
