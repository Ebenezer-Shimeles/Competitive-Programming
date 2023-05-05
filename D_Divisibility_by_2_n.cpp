#include <iostream>
#include <vector>
#include <algorithm>

using std::vector;
using std::sort;
using std::reverse;
using std::cin;
using std::cout;

constexpr char nl = '\n';
int32_t main(){
    int32_t T;
    cin >> T;
    while(T){
        //cout << "-------------------------\n";
        int32_t N;
        cin >> N;
        int32_t twos = 0;
        int32_t available  = 0;
        vector<int32_t> avs = {};
        for(int32_t i =0;i<N;i++){
            uint64_t tmp;
            
            int32_t av_tmp = 0;
            int32_t j = (i+1);
            while(j){
                if(j % 2 == 0){
                    j /=2;
                    available++;
                    av_tmp++;
                }
                else{
                    break;
                }
            }
            avs.push_back(av_tmp);
            cin >> tmp;
            
            while(tmp){

                if(tmp % 2 == 0){
                    tmp /= 2;
                    ++twos;
                }
                else{
                    break;
                }
            }
        }
       
       // cout << N << " " << twos << " " << available<< " " << (int32_t)N-twos<<nl;
        // Needed = N - twos
        if(available < (int32_t)N -  (int32_t)twos){

            cout << - 1;
          
        }
        else{
            int32_t need = N-twos;
            sort(avs.begin(), avs.end());
            //reverse(avs.begin(), avs.end());
            uint32_t i = 0;
            while(avs.size() && need > 0){
                int32_t t = avs.back();
                avs.pop_back();
                need -= t;
                i +=1;
            }
            cout << i;

        }
        cout <<nl;

        T--;
    }
}