#include<iostream>

using namespace std;

char cifra(char letra, int offset){
    int ascii = int(letra) - offset;
    if(ascii < 65){
        ascii += 26;
    }
    return char(ascii);
}

int main(){

    int n;
    string message;
    int offset;

    cin >> n;
    for(int i = 0; i<n; i++){
        cin >> message;
        cin >> offset;
        for(const auto &ch : message){
            cout << cifra(ch, offset);
        }
        cout << '\n';
    }

    return 0;
}