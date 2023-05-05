#include <iostream>
#include <string>
#include <map>
#include <algorithm>
#include <vector>
#include <numeric>
using std::vector;
using std::map;
using std::cout;
using std::cin;
using std::string;
using namespace std;

constexpr char nl = '\n';
template<typename A, typename B>
std::pair<B,A> flip_pair(const std::pair<A,B> &p)
{
    return std::pair<B,A>(p.second, p.first);
}

template<typename A, typename B>
std::multimap<B,A> flip_map(const std::map<A,B> &src)
{
    std::multimap<B,A> dst;
    std::transform(src.begin(), src.end(), std::inserter(dst, dst.begin()), 
                   flip_pair<A,B>);
    return dst;
}

int main(){
    cin.tie(0);  
    std::ios_base::sync_with_stdio(0);
   
    size_t T;
    cin >> T;
    
    while(T){
        //cout << "----------------\n";
        size_t N;
        cin >> N;
        string str;
        cin >> str;
        if(N % 2){
            cout << -1; //This is because the middle will always be equal to itself;
        }
        else{
            map<char, size_t> counts = {};
            bool broke = false;
            for(const char ch : str){
                counts[ch] += 1;
                if(counts[ch] > N/2){
                    cout << -1;
                    broke = true;
                    break;
                }
            }
            map<char, size_t> dups = {};
            uint32_t d = 0;
            if(!broke){
               
                size_t l = 0, r = N-1;
                while (l < r){
                    if(str[l] == str[r]){
                        d++;
                        dups[str[l]] += 1;
                    }
                    l++;
                    r--;
                }
                size_t mx = 0;
                for(auto [ch, num] : dups){
                    mx = max(mx, num);
                }
                cout << max(mx, (size_t)(d+1)/2);
              
        
               
            }
           

        }
        cout <<nl;
        T--;
    }

}