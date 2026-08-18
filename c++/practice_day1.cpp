#include<bits/stdc++.h>
using namespace std;
int main(){
    int input;
    cin>>input;
    vector<string> str;
    for (int j =0; j< input; j++){
	    cin>>str[j-1];
    }
    while (input--){
	    int num=0;
	    num++;
	    auto  str1=str[num-1];
        if (str1.size()<10){
            cout<<str1<< endl;
        }
        else{  
         cout<<str1[0]<<str1.size()-2<<str.back()<<"\n";
         }
    }
    return 0;
}
