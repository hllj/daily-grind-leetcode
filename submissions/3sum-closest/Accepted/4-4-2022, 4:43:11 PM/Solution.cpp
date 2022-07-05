// https://leetcode.com/problems/3sum-closest

class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        int n = nums.size();
        sort(nums.begin(), nums.end());
        int res = int(1e8);
        int ret = -1;
        for(int i = 0; i < n; i++)
            for (int j = i + 1; j < n; j++) {
                int left = j + 1;
                int right = n - 1;
                while (left <= right) {
                    int mid = (left + right) >> 1;
                    int sum3 = nums[i] + nums[j] + nums[mid];
                    int d = sum3 - target;
                    if (abs(d) < res) {
                        res = abs(d);
                        ret = sum3;
                    }
                    if (d < 0) left = mid + 1;
                    else 
                        right = mid - 1;
                }
            }
        return ret;
    }
};