#include<bits/stdc++.h>
using namespace std;
int main(){
	int a, sum =0;
	cin>>a;
	float arr[a];
	for(int i=0;i<a;i++){
		cin>>arr[i];
		sum+=arr[i];	
	
	
	}
	cout<<(float)sum/a;
	
}
