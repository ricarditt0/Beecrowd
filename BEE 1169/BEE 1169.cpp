#include<iostream>
#include<cmath>


using namespace std;

int main (){
    int n ;
    cin >> n;
    for(int i = 0; i<n; i++){
        int termo;
        cin >> termo;
        unsigned long long int an = 1;
        an = 1 * pow(2,termo);
        cout << an/12000 << " kg" << endl;
    }

    return 0;
}