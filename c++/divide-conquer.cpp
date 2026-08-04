#include<iostream>
#include<cmath>
int main(){
    long z ,l,x;
    std::cin>>l;
    for( int i=0; i<l; i++ ){
    std::cin>>x;
    std::cin>>z;
    long m=x/z;

    if(m%z==0){
     std::cout<<"yes";
    }
    else{
     std::cout<<"no";
    }
      }
   return 0;
}
