#include<iostream>
#include<vector>
using namespace std;
int main(){
     int<vector> m ,n;
     cin >> m;
     int k= 0;
     auto<vector> left={};
     auto<vector>  right={};
     for (int j : m){
       if(j<=m[k]) left.push_back(j);
       else  right.push_back(j);
     }
     
     return {};
}
