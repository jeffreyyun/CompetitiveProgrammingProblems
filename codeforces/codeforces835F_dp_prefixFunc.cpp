// Contest 835F: String Compression

#include <bits/stdc++.h>
using namespace std;

const int MX = 8008;
string s;
int n;
int p[MX][MX];
int d[MX];  // compressed length at each char

void computePrefix(int k)
{
    // computes prefix for the suffix k
    for (int i = k + 1; i < n; i++)
    {
        int j = p[k][i-1];
        while (j > 0 && s[i] != s[k + j])
            j = p[k][k + j - 1];
        if (s[i] == s[k + j])
            j++;
        else
            j = 0;
        p[k][i] = j;
    }
}

int len_num (int n) {
    // length (digits) in a number
    int res = 0;
    while (n) {
        n /= 10;
        res++;
    }
    return res;
}

/*
How can we update dp[j] from dp[i] (i < j)? Suppose that we try to represent the substring
from index i to index j - 1 (0-indexed) by writing it as some other string k times. Then this string
has to be the smallest period of the substring, and, where T is the length of the smallest period.

The smallest period of some string t can be calculated as follows: compute prefix-function for t,
and if |t| is divisible by |t| - plast (plast is the last value of prefix-function), then
the length of the smallest period is |t| - plast (if not, then the length of the smallest period is |t|).
*/

int main()
{
    cin >> s;
    n = s.length();
    for (int i = 0; i < n; i++)
    {
        computePrefix(i);
    }
    d[0] = 0;   // no characters to be compressed
    for (int i = 1; i < n + 1; i++)
    {
        // (previous sequence)(d[i-1]) + (new char) or (entire prefix)(i - 1) + (new char)
        d[i] = min(d[i-1] + 2, i + 1);
        for (int j = 0; j < i; j++)
        {
            int pprev = p[j][i-1]; // length of prefix for this substring
            int plen = i - j;      // length of the substring
            // To find length of the actual subsequence, we note any repetition from earlier
            // pprev consists of the subsequence repeated (pprev)/(actual_len) times ... by definition of its prefix #
            if (pprev*2 >= plen && plen % (plen - pprev) == 0)
                plen -= pprev;
            // can update with (previous compress length) + (length of number) + (length of sequence)
            d[i] = min(d[i], d[j] + len_num((i - j)/plen) + plen);
        }
    }
    cout << d[n] << endl;

    return 0;
}