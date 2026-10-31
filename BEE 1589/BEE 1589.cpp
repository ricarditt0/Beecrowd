#include<iostream>

using namespace std;

int main(){

    int t,raio1,raio2;
    cin >> t;

    for(int i; i<t; i++){
        cin >> raio1 >> raio2;
        cout << (raio1 + raio2) << endl;
    }

    return 0;
}