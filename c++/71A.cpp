#include<bits/stdc++.h>
using namespace std;
int main(){
     string words;
     cin>>words;
      if (words.size()<10){
         cout << words <<"\n";
      }
      else{
	int m=words.length();
	  cout<< words[0] <<m-1 <<words[m-1];
      }
return 0;
}

#include <bits/stdc++.h>
using namespace std;

int main() {
	    int n;
	        cin >> n;

		    while (n--) {
			            string word;
				            cin >> word;

					            if (word.length() <= 10) {
							                cout << word << '\n';
									        } else {
											            cout << word[0] << word.length() - 2 << word.back() << '\n';
												            }
						        }
		        return 0;
}
