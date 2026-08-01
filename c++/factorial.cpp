
#include <iostream>
using namespace std;
int main()
{
    int total = 1; //assing the one value
    int n,a ; //for input terms 
    cout << "enter number for factorial :" ;
    cin >> n ;cout<< "\n";
    a = n; // for safe swap
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
/*this one of a recursion using a top ... goto top aproch 
 *in this methode is a one of a easy and finest methode 
 */
