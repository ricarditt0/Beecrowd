#include<iostream>

using namespace std;

int main(){
    int n;
    cin >> n;

    if(n == 0) cout << 'E';
    else if (n < 36) cout << 'D';
    else if (n < 61) cout << 'C';
    else if (n < 86) cout << 'B';
    else if (n >= 86) cout << 'A';
    cout << '\n';
    return 0;
}