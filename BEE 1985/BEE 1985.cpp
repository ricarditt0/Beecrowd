#include<iostream>
#include <iomanip>


using namespace std;

int main(){
    int p,n,q;
    float total = 0;

    cin >> n;
    for(int i = 0; i<n; i++){
        cin >> p >> q;

        switch (p){
        case 1001:
            total += 1.5 * q;
            break;
        case 1002:
            total += 2.5 * q;
            break;
        case 1003:
            total += 3.5 * q;
            break;
        case 1004:
            total += 4.5 * q;
            break;
        case 1005:
            total += 5.5 * q;
            break;
        }
    }
    cout << fixed << setprecision(2) << total << '\n';
}