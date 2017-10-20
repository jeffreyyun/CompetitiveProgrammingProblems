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

	// a/b -> sequence -> (a+b)/b
	// a/b -> parallel -> a/(a+b)
	ll a, b;
	cin >> a >> b;
	ll counter = 0;

	// WHY are the below statements true? Still don't get the intuition.
	// Each necessary resistor represents a step
	// # of steps in Euclidean algorithm
	while(a > 0 && b > 0){		// Calkin-Wilf Tree
		counter += a/b;
		a = a % b;
		swap(a,b);
	}

	cout << counter << endl;	

	return 0;
}