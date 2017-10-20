#include <iostream>
#include <cctype>
#include <cmath>
#include <string>
#include <algorithm>
#include <vector>
#include <climits>
using namespace std;
#define ll long long

int main() {

	ll n;
	cin >> n;
	ll score = n;		// sets to # first removed

	// divides by smallest divisor, adds to score
	for (int i = 2; i*i <= n; i++) {
		while (n % i == 0) {
			n /= i;
			score += n;
		}
	}

	cout << score;
	return 0;
}