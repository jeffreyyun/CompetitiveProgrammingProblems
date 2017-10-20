#include <iostream>
#include <cctype>
#include <cmath>
#include <string>
#include <algorithm>
#include <vector>
#include <climits>
using namespace std;
#define ll long long

// choose ak and delete; all elements == ak+1 an ak-1 also deleted -> ak points
int main() {
	// HOW TO WIN:
	// Start from the bottom.

	ll n, el;
	cin >> n;
	vector<ll> dp(1e5+1,0);
	vector<ll> v(1e5+1,0);		// how many of each number there are
	//vector<int> a(n,0);
	for (int i = 0; i < n; i++) {
		cin >> el;
		//a.push_back(el);
		v[el]++;
	}
	//sort(a.begin(), a.end());
	// dp[1] = 1*v[1];
	// dp[2] = max(2*v[2],dp[1]);

	// dp[i] is max score by taking numbers i or less
	dp[0] = 0;
	dp[1] = v[1] * 1;

	for (int i = 2; i <= 1e5; i++) {
		// max between taking This Number vs. Not Taking
		dp[i] = max((ll)i*v[i] + dp[i-2], dp[i-1]);
		// If we don't take, we are able to take from dp[i-1] since i-1 is not erased!
	}
	cout << dp[n];
    return 0;
}