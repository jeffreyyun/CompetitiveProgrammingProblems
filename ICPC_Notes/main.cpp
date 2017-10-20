//Problem        : Sum Sum Cryptography
//Language       : C++14
//Compiled Using : g++
//Version        : GCC 4.9.1
//Input for your program will be provided from STDIN
//Print out all output from your program to STDOUT

#include <iostream>
#include <string>
#include <algorithm>
#include <climits>
#include <bits/stdc++.h>

using namespace std;

int main() {

    long long N;
    cin >> N;
    cout << N;
    long long MAX = 3000000;

    set<int>ans;
    cout << N;

    for(int X=1; X<sqrt(N); X++) {
        for(int Y=1; Y<sqrt(N-X<<1); Y++) {
            for(int Z=1; Z<sqrt(N-X<<1-Y<<1); Z++)
                if (X<<1 + Y<<1 + Z<<1 == N)
                    ans.insert(X+Y+Z);
        }
    }

    long long sum = 0;
    for (int i : ans) {
    sum += i;
}

    cout << sum;

    return 0;
}
