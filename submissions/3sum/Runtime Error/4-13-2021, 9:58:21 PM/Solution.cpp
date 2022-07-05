// https://leetcode.com/problems/3sum

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector< vector<int> > ret;
        sort(nums.begin(), nums.end());
        for(int i = 0; i < nums.size(); i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            int target = -nums[i];
            int j = i + 1, k = nums.size() - 1;
            while(j < k) {
                if (nums[j] + nums[k] < target) 
                    j++;
                else if (nums[j] + nums[k] > target)
                    k--;
                else {
                    ret.push_back(vector<int>{nums[i],nums[j],nums[k]});
                    while (j < nums.size() && nums[j] == nums[j + 1]) j++;
                    while (k > i && nums[k] == nums[k - 1]) k--;
                    j++;
                    k--;
                }
            }
        }
        return ret;
    }
};