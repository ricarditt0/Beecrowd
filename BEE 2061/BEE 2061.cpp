#include<iostream>

using namespace std;

int main(){

    int m,n;
    string acao;

    cin >> m >> n;
    for(int i = 0; i<n; i++){
        cin >> acao;
        if(acao =="fechou"){
            m++;
        }
        else{
            m--;
        }
    }        
    cout << m << endl;

    return 0;
}