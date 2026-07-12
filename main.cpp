#include <iostream>
using namespace std;
int main()
{
	float num1,num2,sum,average;
	cout << "enter a two num:" ;
	cin >> num1 ;
	cin >> num2 ;
	sum=num1 + num2;
	average=sum/2;
	
	cout << "sum:" << sum << "\n";
	cout << "average:" << average << "\n";
	return 0;
}	

