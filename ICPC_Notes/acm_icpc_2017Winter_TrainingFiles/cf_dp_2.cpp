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

	int n;
	cin >> n;
	int m = 1e9+7;

	/*
	vector<ll> dp(1e7+1, 1);
	vector<ll> v(1e7+1, 1);		// ways to get to vertex
	// dp[i] = number of ways to return to D in i steps

	dp[1] = 0;
	dp[2] = 3;
	v[1] = 1;
	v[2] = 2;
	// dp[3] = 6 (3 options);
	// dp[4] = 21; (6 + 6 + 9(3*3 - D in mid))
	// dp[5] = 60;

	for (int i = 3; i <= n; i++) {
		dp[i] = (v[i-1]*3) % (m);			// three ways to get to D
		v[i] = (dp[i-1]+v[i-1]*2) % (m);	// ways to get to any vertex
	}
	cout << dp[n];
	*/

	// SLIDING WINDOW (memory-saving)
	ll dpt1, dpt2, vt1, vt2;
	dpt1 = 0;
	dpt2 = 3;
	vt1 = 1;
	vt2 = 2;
	for (int i = 2; i <= n; i++) {
		dpt2 = (vt1*3) % (m);			// three ways to get to D
		vt2 = (dpt1+vt1*2) % (m);	    // ways to get to any vertex
		vt1 = vt2;
		dpt1 = dpt2;
	}
	if (n == 1) cout << 0;
	else cout << dpt2;
}