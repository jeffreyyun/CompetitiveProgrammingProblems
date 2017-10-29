class Solution {
public:
    int smallestDistancePair(vector<int>& nums, int k) {
        int N = nums.size();
        int large = 1000000;
        vector<int> cnt(large, 0);
        for (int i = 0; i < N; i++)
            for (int j = i+1; j < N; j++)
                cnt[abs(nums[i]-nums[j])]++;

        for (int i = 0; i < large; i++)
        {
            k -= cnt[i];
            if (k <= 0) return i;
        }
    }
};
