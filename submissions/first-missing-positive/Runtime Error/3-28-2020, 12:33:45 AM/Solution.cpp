// https://leetcode.com/problems/first-missing-positive

class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        int n = nums.size();
        if (n == 0) return 1;
        sort(nums.begin(), nums.end());
        int idx = 0;
        while (nums[idx] < 0 && idx < n) idx++;
        if (idx == n) return 0;
        if (nums[idx] > 1) return 1; 
        for (int i = idx; i < n - 1; i++)
            if (nums[i + 1] - nums[i] > 1) {
                return nums[i] + 1;
            }
        return nums[n - 1] + 1;
    }
};