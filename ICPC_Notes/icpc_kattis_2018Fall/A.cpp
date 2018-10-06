#if 1

// =========== START OF TEMPLATE ==============
#define TESTING

// #include <iostream>
// #include <vector>
// #include <cstdio>
// #include <cmath>
// #include <algorithm>
// #include <set>
// #include <map>
// #include <queue>
// #include <deque>
// #include <string>
// #include <cassert>
// #include <sstream>
#include <bits/stdc++.h>
#define PB push_back
#define MP make_pair
#define sz(v) (ll((v).size()))
#define forn(i,n) for(ll i = 0; i < (n); ++i)
#define forv(i,v) forn(i,sz(v))
#define fors(i,s) for(auto i=(s).begin();i!=(s).end();++i)
#define all(v) (v).begin(), (v).end()
#define max(a,b) (a>b)?a:b
#define min(a,b) (a<b)?a:b
using namespace std;

typedef long long ll;
typedef pair<ll, ll> pii;
typedef vector<ll> vi;
typedef vector<vi> vvi;
int INF = 1000000005;
long long INFF = 1000000000000000005ll;
double PI = acos(-1);

#ifdef TESTING
#define DEBUG fprintf(stderr,"====TESTING====\n")
#define what_is(x) cerr << #x << " is " << x << endl
#define debug(...) fprintf(stderr, __VA_ARGS__)
#define error(args...) { vector<string> _v = split(#args, ','); err(_v.begin(), args); }
vector<string> split(const string& s, char c) {
	vector<string> v;
	stringstream ss(s);
	string x;
	while (getline(ss, x, c))
		v.emplace_back(x);
	return move(v);
}
#else
#define DEBUG
#define what_is(x)
#define debug(...)
#endif

inline void CLOSE () {
    fclose(stdin);
    fclose(stdout);
}

// =========== END OF TEMPLATE ==============

inline void OPEN (string s) {
    freopen ((s + ".in").c_str (), "r", stdin);
    freopen ((s + ".out").c_str (), "w", stdout);
}

int main()
{
    string FNAME = "";
    OPEN(FNAME);
    
    // faster I/O
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int TC, a, b;
    scanf("%d", &q);
    while (TC--)    // do for each test case
    {
        scanf("%d %d", &a, &b);
        
        printf("%d\n", someIntResult);
        
    }
}


#else if 0

{ }

#endif
