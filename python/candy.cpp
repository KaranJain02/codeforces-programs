#include<bits/stdc++.h>
using namespace std;
#define int long long
int32_t main(){
	int t,n;
	float p;
	cin>>t;
    vector<int>power;
    for(int k=2;k<=30;k++){
        power.push_back(pow(2,k)-1);
    }
	for(int i=0;i<t;i++){
		cin>>n;
        int ans;
		for(int k=0;k<power.size();k++){
			if(n%power[k]==0){
				ans=n/power[k];
				break;
			}			
		}
		cout<<ans<<"\n";
	}
    return 0;
}