// https://leetcode.com/problems/jump-game-ii

class Solution {
public:
    int jump(vector<int>& nums) {
        int n = nums.size();
        const int inf = INT_MAX;
        vector <int> f(n);
        for (int i = 0; i < n; i++)
            f[i] = INT_MAX;
        f[0] = 0;
        for (int i = 0; i < n; i++) {
            int step = nums[i];
            for (int j = 0; j <= step; j++)
                if (i + j < n) f[i + j] = min(f[i + j], f[i] + 1);
        }
        return f[n - 1];
    }
};