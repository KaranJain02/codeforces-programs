#include<bits/stdc++.h>
using namespace std;
int main(){
	int x,y,z,p;
	cin>>x>>y>>z;
	p=((x*z*(z+1))/2)-y;
	if(p>0){
		cout<<((x*z*(z+1))/2)-y;
	}
	else{
		cout<<"0";
	}
	
	
	
}
