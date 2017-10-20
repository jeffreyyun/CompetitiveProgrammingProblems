#include <iostream>
#include <string>
#include <cctype>
#include <cmath>
using namespace std;


int main() {
	int n = 0, k = 0;
	string s = "";
	cin >> n >> s;
	for (int i = 0; i < n; i++) {
	    cout << k;
		if (s[i] == 'o' && k % 2 == 0 && i < n-1) {
			k++;
		}
		else if (s[i] == 'g' && k % 2 == 1 && i < n-1) {
			k++;
		}
		else if (k >= 3) {	// 'ogogmogo'
		    cout << " i: " << i << endl;
		    			s = s.substr(0,i+1-k) + "***";
			k = ceil(k/2) * 2 - 1; // 4 -> 3, 3 -> 3
			if (i < n-1) s += s.substr(i+1);
			i -= (k-3);
		}
		else k = 0;
	}
	cout << s;

	return 0;
}

// problem: interview with oleg
