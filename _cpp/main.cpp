#include <bits/stdc++.h>
using namespace std;

const int LARGE = 1e5+8;
int P, x, y;
int p1[2], p2[2];
int pts[LARGE][2]{{0,0}};
int pt[2];

    bool hasAlternatingBits(int n)
    {
        n = (unsigned int) n;
        cout << (n^(n>>1)) <<'.';
        return ((n^(n>>1)) == -1);
    }

int main()
{
    int a;
    for (a = 0; a < 20; a++)
        cout << hasAlternatingBits(a) << ' ';
}
