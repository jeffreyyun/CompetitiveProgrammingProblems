#include <bits/stdc++.h>
using namespace std;
#define pb push_back

int main() {

    // faster I/O
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);



    long long n;
    scanf("%lld", &n);
    vector<long long> factors;
    bool isPrime = false;

    while (n > 1)
    {
        isPrime = true;
        if (n % 2 == 0) {
            n /= 2;
            factors.pb(2);
            continue;
        }
        for (long long i = 3; i <= floor(sqrt(n))+2; i += 2)
        {
            if (n % i == 0)
            {
                n /= i;
                factors.pb(i);
                isPrime = false;
                break;
            }
        }
       if (isPrime)
       {
           factors.pb(n);
           break;
       }
    }

    for (long long f : factors)
        printf("%lld ", f);
    printf("\n");

    return 0;
}
