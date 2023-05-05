#include <iostream>
#include <vector>
#include <numeric>
#include <map>

using std::map;
using std::accumulate;
using std::cin;
using std::vector;
using std::uint32_t;
using std::uint64_t;
using std::cout;
constexpr char nl = '\n';
int main(){
    std::ios_base::sync_with_stdio(0);
    std::cin.tie(0);
    uint32_t T;
    std::cin >> T;
    while(T){
        map<uint64_t, size_t> primes = {};
        size_t N;
        cin >> N;
        uint64_t tmp;
        for(int i=0;i<N;i++){ 
            cin >> tmp;
            size_t j = 2;
            while(j * j <= tmp){
                 while(tmp % j == 0)
                 {
                    primes[j] += 1;
                    tmp /= j;
                 }
                 j += 1;
            }
            if(tmp > 1){
                primes[tmp] += 1;
            }
        }
        size_t sz = 0;
        size_t ans = 0;
        for(auto [prime, count ] : primes){
            if(count > 1){
               ans += count/2;
               sz += (count % 2);
            }
            else{
                sz += count;
            }

        }
        ans += sz/3;
        cout << ans;
   
        cout << nl;       
        T --;
    }
}