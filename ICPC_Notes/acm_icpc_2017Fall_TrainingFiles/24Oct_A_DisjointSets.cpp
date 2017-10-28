#include <bits/stdc++.h>
#include <string>
using namespace std;
#define pb push_back

// Not accepted - TLE
// How to succeed: adapt the Stanford notebook functions (below)
// for this problem

int find(vector<int>&C, int x)
{
    return (C[x] == x) ? x : C[x] = find(C, C[x]);
}
void merge(vector<int> &C, int x, int y)
{
    C[find(C, x)] = find(C, y);
}


int main() {

    // faster I/O
    //ios_base::sync_with_stdio(false);
    //cin.tie(NULL);

    long long NC;
    scanf("%lld", &NC);

    vector<int>C(NC+1);
    string term;
    int a,b;
    int s;

    for (int i = 0; i <= NC; i++)
        C[i] = i;

    while(cin >> term)
    {
        if (term == "union")
        {
            scanf("%d %d",&a,&b);
            merge(C, a, b);
        }
        else if (term == "get")   // "get"
        {
            scanf("%d",&s);
            s = find(C,s);
            int m_min = 300005, m_max = 0, size = 0;
            for (int i = 0; i < NC+1; i++)
            {
                if (find(C,i) == s)
                {
                    m_min = min(m_min, i);
                    m_max = max(m_max, i);
                    size++;
                }
            }
            printf("%d %d %d\n", m_min, m_max, size);
        }
        else if (cin.eof())
            break;
    }

    return 0;
}
