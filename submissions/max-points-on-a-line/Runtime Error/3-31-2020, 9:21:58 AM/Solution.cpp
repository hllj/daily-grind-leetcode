// https://leetcode.com/problems/max-points-on-a-line

class Solution {
public:
    int maxPoints(vector<vector<int>>& points) {
        int res = 0;
        int n = points.size();
        if (n == 0) return 0;
        if (n == 1) return 1;
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++) 
            if (i != j) {
                int cnt = 0;
                int x0 = points[i][0];
                int y0 = points[i][1];
                int x1 = points[j][0];
                int y1 = points[j][1];
                int value = (y0 - y1) * x0 + (x1 - x0) * y0;
                for (int k = 0; k < n; k++) {
                    int x = points[k][0];
                    int y = points[k][1];
                    if ((y0 - y1) * x + (x1 - x0) * y == value) cnt++;
                }
                res = max(res, cnt);
            }
        return res;
    }
};