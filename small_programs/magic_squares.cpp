// Inspiration: https://wordsandbuttons.online/challenge_your_performance_intuition_with_cpp_magic_squares.html
//
#include <chrono>
#include <iostream>

using namespace std;

bool check_if_magic(const std::string& square){


    return false;
}


// this generates all possible combinations
// of 1-9 digits that may or may not
// form a magic square
static string buffer = "000000000";
void generate_or_check(int index_or_check = 8)
{
  if(index_or_check == -1){
    if(check_if_magic(buffer))
      cout << buffer << " ";
    return;
  }

  for(auto i = 1u; i < 10; ++i){
    buffer[index_or_check] = '0' + i;
    generate_or_check(index_or_check-1);
  }
}

int main(void){

    auto start = chrono::system_clock::now();
    generate_or_check();
    auto end = chrono::system_clock::now();
    chrono::duration<double> diff = end - start;
    cout << diff.count() << endl;
    return 0;
}
