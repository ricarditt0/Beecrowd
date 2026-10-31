#include<iostream>

using namespace std;

int main (){

    int portion[5] = {300,1500,600,1000,150};
    int total = 225;
    int servidas = 0;

    for(int i = 0; i<5; i++){
        cin >> servidas;
        total += servidas * portion[i];
    }
    cout << total << '\n';

    return 0;
}