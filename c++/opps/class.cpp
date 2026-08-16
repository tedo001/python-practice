#include<iostream>
#include<string>
using namespace std;
class mani {
	public:
		int rollno;
		int phno;

		string name;
	void display(){
	cout<< "name: "<< name <<endl;
	cout << "roolNo: " <<rollno <<endl;
	}	
         private:
               int enroll_id;
};


int main(){
     mani raj;//object 
     raj.rollno=3234;
     raj.name="gopal";
     cout<< raj.name <<'\n';
     raj.display();
  //   raj.enroll_id =1212;
//	cout << raj.enroll_id;
     mani jani;// object 

return 0;
}


