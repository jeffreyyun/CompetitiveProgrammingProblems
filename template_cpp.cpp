#if 1

// =========== START OF TEMPLATE ==============
#define TESTING
#include <bits/stdc++.h>
using namespace std;

#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define REP(i, n) FOR(i, 0, n)

typedef long long ll;
int INF = 1000000005;
long long INFF = 1000000000000000005ll;
double PI = acos(-1);

#ifdef TESTING
#define DEBUG fprintf(stderr,"====TESTING====\n")
#define what_is(x) cerr << #x << " is " << x << endl
#define debug(...) fprintf(stderr, __VA_ARGS__)
#else
#define DEBUG
#define what_is(x)
#define debug(...)
#endif

#define error(args...) { vector<string> _v = split(#args, ','); err(_v.begin(), args); }
vector<string> split(const string& s, char c) {
    vector<string> v;
    stringstream ss(s);
    string x;
    while (getline(ss, x, c))
        v.emplace_back(x);
    return move(v);
}
void err(vector<string>::iterator it) {}
template<typename T, typename... Args>
void err(vector<string>::iterator it, T a, Args... args) {
    cerr << it -> substr((*it)[0] == ' ', it -> length()) << " = " << a << '\n';
    err(++it, args...);
}

inline void OPEN (string s) {
    freopen ((s + ".in").c_str (), "r", stdin);
    freopen ((s + ".out").c_str (), "w", stdout);
}

inline void CLOSE () {
    fclose(stdin);
    fclose(stdout);
}

// =========== END OF TEMPLATE ==============

int main()
{
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
