// https://leetcode.com/problems/count-of-range-sum

class Solution {
public:
    int countRangeSum(vector<int>& nums, int lower, int upper) {
        int n = nums.size();
        map<long long, long long> m;
        m.insert(make_pair(0, 1));
        long long sum = 0;
        long long cnt = 0;
        for (int i = 0; i < n; i++) {
            sum += (long long) nums[i];
            for (long long r = lower; r <= upper; r++)
                if (m.find(sum - r) != m.end()) {
                    cnt += m[sum - r];
                }
            if (m.find(sum) == m.end()) m[sum] = 1;
            else m[sum]++;
        }
        return cnt;
    }
};