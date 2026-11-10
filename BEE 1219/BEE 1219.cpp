#include<iostream>
#include<cmath>
#include <iomanip>


using namespace std;

int main(){
    const double PI = 3.1415926535897;
    int a,b,c;
    while(cin >> a >> b >> c ){
        double p = (a + b + c)/2.0;
        double triangle_area = sqrt(p*(p-a)*(p-b)*(p-c));
        double raio = triangle_area/p;
        double circunference_area = PI * raio * raio;
        double raio_externo = (a*b*c)/(4.0*triangle_area);
        double circunference_area_externo = PI * raio_externo * raio_externo;
        cout << fixed << setprecision(4) << circunference_area_externo - triangle_area << " " << triangle_area - circunference_area << " " << circunference_area << endl;
    }
    return 0;
}