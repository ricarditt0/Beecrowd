#include<iostream>

using namespace std;

int main(){
    int n;
    int s;
    int b;
    int menor;
    cin >> n >> s;
    menor = s;
    for(int i = 0; i<n; i++){
        cin >> b;
        s += b;
        if(s < menor) menor = s;
    }
    cout << menor << '\n';
}