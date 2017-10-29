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

    int N;
    vector<int> nums;

    scanf("")

    return 0;
}



class Solution {
public:
    int smallestDistancePair(vector<int>& nums, int k) {
        map<int, int> diffs;
        N = len(nums);
        for (int i = 0; i < N; i++)
            for (int j = i+1; j < N; j++)
            {
                int d = abs(nums[j]-nums[i]);
                if (diffs.count(d) > 0)
                    diffs[d] += 1;
                else
                    diffs[d] = 1;
            }

        for(map<int, int>::iterator iter = diffs.begin(); iter != diffs.end(); ++iter)
        {
            k -= iter->second;
            if (k <= 0)
                return iter->first;
        }

    }
};