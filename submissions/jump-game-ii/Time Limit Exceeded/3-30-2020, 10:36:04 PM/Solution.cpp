// https://leetcode.com/problems/jump-game-ii

class Solution {
public:
    int jump(vector<int>& nums) {
        int n = nums.size();
        const int inf = INT_MAX;
        vector <long long> f(n);
        for (int i = 0; i < n; i++)
            f[i] = INT_MAX;
        f[0] = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++)
                if (nums[j] + j >= i)
                    f[i] = min(f[i], f[j] + 1);
        }
        return f[n - 1];
    }
};