#include <bits/stdc++.h>
using namespace std;

int main() {

    // faster I/O
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    const long long BIGNUM = 1000055;
    vector<bool>primes(BIGNUM,true);

    primes[1] = false;

    for (int i = 4; i < BIGNUM; i +=2)
        primes[i] = false;

    for (int n = 3; n < BIGNUM; n += 2)
        for (int i = n*2; i < BIGNUM; i += n)
            primes[i] = false;


    int TC, n;
    scanf("%d", &TC);
    while (TC--)
    {
        scanf("%d", &n);
        if (primes[n]) printf("%s\n", "YES");
        else printf("%s\n", "NO");
    }

    return 0;
}
