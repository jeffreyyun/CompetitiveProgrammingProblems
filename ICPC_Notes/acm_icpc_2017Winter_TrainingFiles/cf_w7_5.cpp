#include <iostream>
#include <cctype>
#include <cmath>
#include <string>
#include <algorithm>
#include <vector>
#include <climits>
using namespace std;
#define ll long long

bool isPrime(int s) {
	// sieves up to 10^6 ... could be faster???
	if (s % 2 == 0) return false;
	for (int i = 3; i*i < s; i+=2) {
		if (s % i == 0) {
			return false;
		}
	}
	return true;
}

int main() {
	// Returns if has 3 divisors -- i.e. perfect squares of primes
	ll n, x;
	cin >> n;
	for (ll i = 0; i < n; i++) {
		cin >> x;
		ll s = round(sqrt(x));
		if (s*s == x) {
			if (isPrime(s)) cout << "YES";
			else cout << "NO";
		}
		else cout << "NO";
	}
	return 0;
}