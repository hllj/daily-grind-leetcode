// https://leetcode.com/problems/maximum-gap

class Solution {
public:
    int maximumGap(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        int res = 0;
        for (int i = 0; i < n - 1; i++)
            res = max(res, nums[i + 1] - nums[i]);
        return res;
    }
};