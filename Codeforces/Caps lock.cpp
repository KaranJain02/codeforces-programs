#include<bits/stdc++.h>
using namespace std;
int main(){
	string t;
	cin>>t;
	int count,pount;
	count=0;
	pount=0;
	for(int i=0;i<t.length();i++){
		if(t[i]>='A' && t[i]<='Z'){
			if(t[0]>='A' && t[0]<='Z'){
				count++;
			}
			else{
				pount++;
			}
		}
			
	}
	if(count==t.length()){
		transform(t.begin(),t.end(),t.begin(),::tolower);
		cout<<t;
	}	
	else if(pount==t.length()-1){
		transform(t.begin(),t.end(),t.begin(),::tolower);
		t[0]=toupper(t[0]);
		cout<<t;
	}
	else{
		cout<<t;
	}

	
}
