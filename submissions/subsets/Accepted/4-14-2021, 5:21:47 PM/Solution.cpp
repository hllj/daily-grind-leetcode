// https://leetcode.com/problems/subsets

class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        int n = nums.size();
        int low = 0;
        int high = (1 << n) - 1;
        vector< vector<int> > ret;
        for(int st = low; st <= high; st++) {
            vector<int> subset;
            for(int i = 0; i < n; i++)
                if (((st >> i) & 1) == 1) subset.push_back(nums[i]);
            ret.push_back(subset);
        }
        return ret;
    }
};