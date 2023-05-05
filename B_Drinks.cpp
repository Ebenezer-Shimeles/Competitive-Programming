#include <bits/stdc++.h>
#define ll long long

using namespace std;
int main(){
    int N;
    cin >> N;
    vector<int> percents = {};
    percents.reserve(N);
    for(int i=0;i<N;i++){
        int pct;
        cin >> pct;
        percents.push_back(pct);
    }
    double sum = accumulate(percents.begin(), percents.end(), 10);
    cout << sum/N;


}