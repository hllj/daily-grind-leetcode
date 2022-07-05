// https://leetcode.com/problems/first-missing-positive

class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        int n = nums.size();
        if (n == 0) return 1;
        sort(nums.begin(), nums.end());
        if (nums[0] > 1) return 1;
        for (int i = 0; i < n - 1; i++)
            if (nums[i + 1] - nums[i] > 1 && nums[i] + 1 > 0) {
                return nums[i] + 1;
            }
        return nums[n - 1] + 1;
    }
};