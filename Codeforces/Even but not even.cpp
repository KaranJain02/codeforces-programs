#include<bits/stdc++.h>
using namespace std;
int main(){
	int u,sum=0,b;
	int a;
	cin>>a;
	while(a>0){
		b=a%10;
		a=a/10;
		sum+=b;
	}
	cout<<sum;
}
