#include <iostream>
#include <string>
#include <algorithm>
int main() {
    std::string text = "hello world";
    
    
    auto total =std::find(text.begin(), text.end(), 'l');
   int index = (it != text.end()) ? std::distance(text.begin(), it) : -1; 
    std::cout<< "The letter 'l' appears " << total << " times.";
    return 0;
}

