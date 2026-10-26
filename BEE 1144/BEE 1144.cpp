#include<iostream>

using namespace std;

int main(){
    int n;
    int quadrado;
    int cubo;
    cin >> n;
    for(int i = 1; i <= n; i++){
        quadrado = i * i;
        cubo = i*i*i;

        cout << i << ' ' << quadrado << ' ' << cubo << '\n';
        cout << i << ' ' << quadrado + 1 << ' ' << cubo + 1 << '\n';
    }//for
}