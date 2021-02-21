#include<bits/stdc++.h>
using namespace std;
int main(){
	ios::sync_with_stdio(0);
	cin.tie(0);
	int t,a,b;
	cin>>t;
	
	for(int i = 0; i<t; i++){
		cin>>a>>b;
		if(a>=2*b){
			cout<<a*a<<endl;
		}
		else if(b<=a and a<2*b){
			cout<<4*b*b<<endl;
		}
		else if(b>=2*a){
			cout<<b*b<<endl;
		}
		else{
			cout<<4*a*a<<endl;
		}
	}
	
	
}
