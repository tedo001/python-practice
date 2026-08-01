
#include <iostream>
using namespace std;
int main()
{
    int total = 1;
    int n,a ;
    cout << "enter number for factorial :" ;
    cin >> n ;cout<< "\n";
    a = n;
top:
    if (a != 0)
    {
        total *= a;
        a -= 1;
        
        goto top;
    }

    cout << "factorial of " << n << " is " <<total;

    return 0;
}
