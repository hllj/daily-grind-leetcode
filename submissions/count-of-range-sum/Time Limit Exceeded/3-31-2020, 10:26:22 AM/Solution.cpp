// https://leetcode.com/problems/count-of-range-sum

class Solution {
public:
    int countRangeSum(vector<int>& nums, int lower, int upper) {
        int n = nums.size();
        map<long long, int> m;
        m.insert(make_pair(0, 1));
        long long sum = 0;
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            sum += (long long) nums[i];
            for (long long r = lower; r <= upper; r++)
                if (m.find(sum - r) != m.end()) {
                    cnt += m[sum - r];
                }
            m[sum]++;
        }
        return cnt;
    }
};