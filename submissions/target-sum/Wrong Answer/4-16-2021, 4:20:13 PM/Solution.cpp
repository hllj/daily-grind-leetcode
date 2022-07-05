// https://leetcode.com/problems/target-sum

class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int target) {
        int sum = 0;
        int n = nums.size();
        for(int i = 0; i < n; i++) sum += nums[i];
        if (target > sum) return 0;
        if ((target + sum) % 2 != 0) return 0;
        int pos = (target + sum) / 2;
        int dp[n + 1][pos + 10];
        for(int j = 1; j <= pos; j++)
            dp[0][j] = 0;
        for(int i = 1; i <= n; i++)
            dp[i][0] = 1;
        dp[0][0] = 1;
        for(int i = 1; i <= n; i++) {
            for(int j = 1; j <= pos; j++) {
                dp[i][j] = 0;
                if (j >= nums[i - 1]) dp[i][j] += dp[i - 1][j - nums[i - 1]];
                dp[i][j] += dp[i - 1][j];
            }
        }
        return dp[n][pos];
    }
};