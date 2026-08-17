#include<iostream>
#include<string>
#include<ctime>
using namespace std;
 int main(){
       string girls[2][3]={{"sabi","nira","sabi"},
	                {"arika","nira","sabi"}};
        srand(time(0));
	int num =rand()%2;
       cout<< girls[num][num] << "\n";


       return 0;
}
