#include<bits/stdc++.h>
using namespace std;
int main(){
	long long int n,t,u;
	cin>>n>>t;
	u=t*(pow(10,n-1));
	if(n==1 && t==10){
		cout<<-1;
	}
	else{
		cout<<(long long)(u+t);
	}
}
