// https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array

class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int n = nums.size();
        int low = int(lower_bound(nums.begin(), nums.end(), target) - nums.begin());
        int high = int(upper_bound(nums.begin(), nums.end(), target) - nums.begin()) - 1;
        vector<int> ret;
        if (low >= 0 && low < n && nums[low] == target) ret.push_back(low);
            else ret.push_back(-1);
        if (high >= 0 && high < n && nums[high] == target) ret.push_back(high);
            else ret.push_back(-1);
        return ret;
    }
};