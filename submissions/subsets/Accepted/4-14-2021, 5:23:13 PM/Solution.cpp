// https://leetcode.com/problems/subsets

class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector< vector<int> > ret;
        int i;
        for(int st = 0; st < (1 << nums.size()); st++) {
            vector<int> subset;
            for(i = 0; i < nums.size(); i++)
                if (((st >> i) & 1) == 1) subset.push_back(nums[i]);
            ret.push_back(subset);
        }
        return ret;
    }
};