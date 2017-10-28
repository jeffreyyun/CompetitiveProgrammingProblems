#include <bits/stdc++.h>
using namespace std;
#define pb push_back

vector<long long> nums;

bool tryFact(long long f)
{
    for (long long n: nums)
    {
        if (n % f != 0)
            return false;
    }
    return true;
}

int main() {

    // faster I/O
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int NC;
    long long n;
    long long m_max = 0;
    scanf("%d", &NC);
    for (int i = 0; i < NC; i++)
    {
        scanf("%lld", &n);
        nums.push_back(n);
        m_max = max(m_max, n);
    }
    long long GCD = 1;

    bool found = true;
    while (found)
    {
        found = false;
        if (tryFact(2))
        {
            found = true;
            GCD *= 2;
            // reduce the problem
            for (int j=0; j < NC; j++)
            {
                nums[j] /= 2;
            }
        }
        for (int i = 3; i <= m_max; i+=2)
        {
            if (tryFact(i))
            {
                found = true;
                GCD *= i;
                // reduce the problem
                m_max = 0;
                for (int j=0; j < NC; j++)
                {
                    nums[j] /= i;
                    m_max = max(m_max, nums[j]);
                }
                break;
            }
        }
    }

    printf("%lld\n", GCD);

    return 0;
}
