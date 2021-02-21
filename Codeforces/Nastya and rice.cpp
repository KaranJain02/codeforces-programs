#include<bits/stdc++.h>
using namespace std;
int main(){
	int t,a,b,c,d,n;
	cin>>t;
	for(int i =0;i<t;i++){
		cin>>n>>a>>b>>c>>d;
		if((c-d)<=n*(a-b) && n*(a-b)<=(c+d) && (c+d)<=n*(a+b)){
			cout<<"YES"<<endl;
		}
		else if((c-d)<=n*(a-b) && n*(a-b)<=n*(a+b) && n*(a+b)<=(c+d)){
			cout<<"YES"<<endl;
		}
		else if(n*(a-b)<=(c-d) && (c-d)<=n*(a+b) && n*(a+b)<=(c+d)){
			cout<<"YES"<<endl;
		}
		else if(n*(a-b)<=(c-d) && (c-d)<=(c+d) && (c+d)<=n*(a+b)){
			cout<<"YES"<<endl;
		}
		else{
			cout<<"NO"<<endl;
		}
	}
}
