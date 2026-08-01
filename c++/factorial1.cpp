#include<iostream>
using namespace std;
int main(){
       int rec=0;
       int n ,m;
       cout <<"enter the input for a recursion : ";
       cin >> n  ;
       m=n;
       if(m>1){
         rec = rec*m;
         return (m-1);
       }
     cout <<"factorial num is :"<<rec<<"of"<<m;

return 0; 
}

       

