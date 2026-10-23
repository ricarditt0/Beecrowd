#include <iostream>
#include <vector>
#include <algorithm>
#include <utility>

using namespace std;


long long distancia_quadratica(pair<int,int> a , pair<int,int> b){
    long long dx = a.first - b.first;
    long long dy = a.second - b.second;
    return (dx*dx) + (dy*dy);
}

int main(){
    int n;
    
    while(cin >> n && n != 0){
        vector<pair<int,int>> pontos(n);
        for(int i = 0; i<n ; i++){
            cin >> pontos[i].first >> pontos[i].second;
        }

        long long resposta = 0;
        for(int i = 0; i<n ; i++){
            vector<long long> distancias;
            distancias.reserve(n-1);

            for(int j = 0; j<n ; j++){
                if (i == j) continue ;
                distancias.push_back(distancia_quadratica(pontos[i],pontos[j]));
            }

            sort(distancias.begin(),distancias.end());
            int k = 1;
            for(int j = 1 ; j<(int)distancias.size() ; j++){
                if(distancias[j]==distancias[j-1]) k++;
                else{
                    resposta += k * (k-1)/2;
                    k = 1;
                }
            }
            resposta += k * (k-1)/2;
        }
        cout << resposta << '\n';
    }
    return 0;
}