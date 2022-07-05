// https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array

class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int n = nums.size();
        int low = int(lower_bound(nums.begin(), nums.end(), target) - nums.begin());
        int high = int(upper_bound(nums.begin(), nums.end(), target) - nums.begin()) - 1;
        vector<int> ret;
        if (low >= 0 && low < n) ret.push_back(low);
        if (high >= 0 && high < n) ret.push_back(high);
        return ret;
    }
};