// https://leetcode.com/problems/frog-jump

class Solution {
public:
    bool canCross(vector<int>& stones) {
        int n = stones.size();
        int f[n];
        for (int i = 0; i < n; i++)
            f[i] = -1;
        f[0] = 0;
        bool res = true;
        for (int i = 0; i < n; i++)
            if (f[i] == -1) {
                res = false;
                break;
            } else {
                int k = f[i];
                for (int j = k - 1; j <= k + 1; j++) {
                    int next = stones[i] + j;
                    int left = 0;
                    int right = n- 1;
                    while (left <= right) {
                        int mid = (left + right) >> 1;
                        if (stones[mid] == next) {
                            f[mid] = j;
                        }
                        if (stones[mid] > next) right = mid - 1;
                        else left = mid + 1;
                    }
                }
            }
        return (f[n - 1] > 0);
    }
};