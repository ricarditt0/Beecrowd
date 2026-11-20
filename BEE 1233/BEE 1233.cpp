#include<iostream>
#include<vector>

using namespace std;

vector<int> generatePrimes() {
    const int MAX = 46340;

    vector<bool> isPrime(MAX + 1, true);
    vector<int> primes;

    isPrime[0] = isPrime[1] = false;

    for (int i = 2; i * i <= MAX; i++) {
        if (isPrime[i]) {
            for (int j = i * i; j <= MAX; j += i) {
                isPrime[j] = false;
            }
        }
    }

    for (int i = 2; i <= MAX; i++) {
        if (isPrime[i]) {
            primes.push_back(i);
        }
    }

    return primes;
}



vector<int> fatoring(int n, const vector<int>& primes){
    vector<int> factors;

    for (int i:primes){
        if(i*i > n){
            break;
        }
        if(n%i == 0){
            factors.push_back(i);
            while(n % i == 0){
                n /= i;
            }
        }
    }
    if (n > 1){
        factors.push_back(n);
    }

    return factors;
}


int main(){
    vector<int> primes = generatePrimes();


    int n, original;
    vector<int> factors;
    while (cin >> n){
        original = n;
        factors = fatoring(n,primes);
        for(auto i:factors){
            original -= original/i;
        }
        cout << original/2 << endl;
    }

    return 0;
}