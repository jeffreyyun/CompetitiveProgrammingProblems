// Prob 2

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

	// find the kth smallest divisor of n
	ll n, k;
	cin >> n >> k;

	vector<ll> d;

	for (ll i = 1; i*i <= n; i++) {
		if (n % i == 0) {
			// i is divisor, n/i is divisor
			d.push_back(i);
			if (i != n/i) d.push_back(n/i);
		}
	}
	sort(d.begin(), d.end());

	if (d.size() < k) cout << -1;
	else cout << d[k-1];

	return 0;
}