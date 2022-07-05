// https://leetcode.com/problems/first-missing-positive

class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        int n = nums.size();
        if (n == 0) return 1;
        sort(nums.begin(), nums.end());
        int idx = -1;
        for (int i = 0; i < n; i++)
            if (nums[i] >= 0) {
                idx = i;
                break;
            } 
        if (idx == -1) return 1;
        if (nums[idx] > 1) return 1; 
        for (int i = idx; i < n - 1; i++)
            if (nums[i + 1] - nums[i] > 1) {
                return nums[i] + 1;
            }
        return nums[n - 1] + 1;
    }
};