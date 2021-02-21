#include<bits/stdc++.h>
using namespace std;
int main(){
	int x,y;
	cin>>x>>y;
	if(x%2==1 && y%2==1){
		cout<<((x*y)-1)/2;		
	}
	else{
		cout<<(x*y)/2;
	}
}

