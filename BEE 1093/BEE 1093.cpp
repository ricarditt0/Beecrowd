#include<iostream>
#include<cmath>
#include <iomanip>


using namespace std;

int main(){
    int ev1 ,ev2 , d, atk;
    while (cin >> ev1 >> ev2 >> atk >> d && (ev1 || ev2 || atk || d)){
        double p = (6.0-double(atk))/6.0;
        double q = 1-p;

        double m1 = (ev2 + d - 1) / d;
        double m2 = (ev1 + d - 1) / d;

        double chance;

        if(atk == 3){
            chance = m2 / (m1 + m2);
        }else{
            chance = (1 - pow((p/q),m2)) / (1 - pow((p/q),(m1+m2)));
        }

        cout << fixed << setprecision(1) << chance * 100.0 << endl ;

    }

    return 0;
}