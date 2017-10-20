// Dynamic Programming

// FIRST EXAMPLE
// First we have coins of value 1, 2, 4
// How many ways to sum to 10?

// ALGORITHM: 
// dp[i] = dp[i-1]+dp[i-2]+dp[i-4]

// EX.   dp[5] = dp[4]+dp[3]+dp[1]
// See, if we use 1 as LAST coin, we look for dp[4], # ways to form 4
// 2 -> dp[3] before it, 4 -> dp[1] before it, etc.

// OUR BASE CASES
// dp[0] = 0, dp[1] = 1, dp[2] = 2, dp[3] = 2;

// OUR PROCESS
// 1. Define subproblems
// 2. Find the recurrence relation
// 3. Deal with base cases

// SECOND EXAMPLE
// We look for the LONGEST INCREASING SUBSEQUENCE
// dp[i] = longest up to position i

// RR: 
// increment i
// dp[i] = max(dp[j] + 1) for all j < i and a[j] < a[i]

// BASE CASES
// dp[1] = 1

// TECHNIQUE - SLIDING WINDOW
// We only need to save the values the current value depends on
// (We could discard of the rest)


#include <iostream>
#include <cctype>
#include <cmath>
#include <string>
#include <algorithm>
#include <vector>
#include <climits>
using namespace std;

int main() {
	// Goal: Find # of distinct integers staying on positions
	int n, m, el;
	cin >> n >> m;
	vector<int> a;
	for (int i = 0; i < n; i++) {
		cin >> el;
		a.push_back(el);
	}
	// dp[i] = the distinct digits starting from ith digit
	vector<int> dp(n, 0);
	vector<bool> seen(1e5 + 1, false);
	seen[v[n-1]] = true;
	dp[n-1] = 1;

	for (int i = n-2; i >= 0; i--) {
		if (seen[v[i]])
			dp[i] = dp[i+1];
		else {
			dp[i] = dp[i+1] + 1;
			seen[v[i]] = true;
		}
	}

	for (int i = 0; i < m; i++) {
		cin >> el;
		cout << dp[el-1] << endl;
	}

	return 0;
}