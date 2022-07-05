// https://leetcode.com/problems/4sum

class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        int n = nums.size();
        sort(nums.begin(), nums.end());
        vector< vector<int> > ret;
        for(int i = 0; i < n; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            int j = i + 1;
            for(; j < n;) {
                int v = nums[i] + nums[j];
                int l = j + 1;
                int k = n - 1;
                cout << "l : " << l << "\n";
                cout << "k : " << k << "\n";
                while(l < k) {
                    cout << (v+ nums[l] + nums[k]) << "\n";
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
                while (j + 1 < n && nums[j + 1] == nums[j]) j++;
                j++;
            }
        }
        return ret;
    }
};