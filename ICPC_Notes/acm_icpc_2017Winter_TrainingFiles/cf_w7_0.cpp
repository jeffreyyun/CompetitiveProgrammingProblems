// Num of divisors of n is provably at most n**(1/3) <-- most ints needed to allocate


#include <iostream>
#include <cctype>
#include <cmath>
#include <string>
#include <algorithm>
#include <vector>
#include <climits>
using namespace std;
#define ll long long

int findNumDivisors(int n) {
	// Finds Number of Divisors
	int count = 0;
	for (int i = 1; i*i <= n; i++) {
		if (n % i == 0) {
			// i is divisor, n/i is divisor
			if (i*i == n) count++;
			else count+=2;
		}
	}
	return count;
}

vector<int> findPrimeDivisors(int n) {
	// Finds Prime Divisors
	vector<int> primes(pow(n,1/3));
	int count = 0;
	int m = n;
	for (int i = 3; i*i <= n; i++) {	// ex. 26 -> adds 2 -> 13
		while (m % i == 0) {
			m /= i;
			primes.push_back(i);
		}
	}
	if (m > 1) {		// ex. 13
		primes.push_back(m);
	}
	return primes;
}


int main() {


	// Finds Prime Divisors
}