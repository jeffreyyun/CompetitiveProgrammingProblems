#include <bits/stdc++.h>
using namespace std;
 
int main() {
 
    // faster I/O
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
 
    freopen("folding.in", "r", stdin);
    freopen("folding.out", "w", stdout);
 
    long long a,b,aa,bb,ca,cb,ta,tb,ans,ans2;
    scanf("%lld %lld", &a, &b);
    scanf("%lld %lld", &aa, &bb);
 
    ca = min(a,b);
    cb = max(a,b);
    ta = min(aa,bb);
    tb = max(aa,bb);
 
    if (ca < ta or cb < tb)
    {
        printf("%d\n", -1);
        return 0;
    }
 
    ans = ceil(log2(1.0*ca/ta)) + ceil(log2(1.0*cb/tb));
    ans2 = ceil(log2(1.0*cb/ta)) + ceil(log2(1.0*ca/tb));
    if (ca >= tb)
        ans = min(ans, ans2);
 
    printf("%lld\n", ans);
    return 0;
 
 
}
