#include <iostream>
#include <string>
#include <algorithm>

int main() {
    std::string text = "hello world";
    
    // Count occurrences of the letter 'l'
    int total = std::count(text.begin(), text.end(), 'l');
    
    std::cout << "The letter 'l' appears " << total << " times.";
    return 0;
}

