// https://leetcode.com/problems/4sum

class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        int n = nums.size();
        sort(nums.begin(), nums.end());
        vector< vector<int> > ret;
        for(int i = 0; i < n; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            for(int j = i + 1; j < n; j++) {
                if (j > 0 && nums[j] == nums[j - 1]) continue;
                int v = nums[i] + nums[j];
                int l = j + 1;
                int k = n - 1;
                while(l < k) {
                    if (v + nums[l] + nums[k] < target) l++;
                    else if (v + nums[l] + nums[k] > target) k--;
                    else if (v + nums[l] + nums[k] == target) {
                        ret.push_back(vector<int>{nums[i], nums[j], nums[l], nums[k]});
                        while (l < k && nums[l] == nums[l + 1]) l++;
                        while (l < k && nums[k] == nums[k - 1]) k--;
                        l++;
                        k--;
                    }
                }
            }
        }
        return ret;
    }
};