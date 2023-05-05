#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>
#include <numeric>

using namespace std;
uint64_t GetMax(const vector<uint64_t>& a, 
                const uint64_t T, uint64_t s, size_t N, size_t l, size_t r){
    if(l > r){
        return 0;
    }
    while(s > T && l<=r){
        N -=1;
        if (a[l] > a[r]){
            s -= a[l];
            l += 1;
        }
        else if (a[r] > a[l]){
                s -= a[r];
                r -= 1;
        }
        else{
             if(s - a[l] <= T){
                return N;
             }
             return GetMax(a, T, s-(a[l]*2), N-1, l+1, r-1);
        }
    }
    return N;
}
int main(){
    cin.tie(0);
    ios_base::sync_with_stdio(0);
    size_t N, T;
    cin >> N >> T;
    vector<uint64_t> nums(N);
    for(int i=1;i<N+1;i++){
        cin >> nums[i-1];
        //cout << nums[i-1];
    }
    uint64_t s = accumulate(nums.begin(), nums.end(), 0);
    cout << GetMax(nums, T, s, N, 0, N-1);
    
}