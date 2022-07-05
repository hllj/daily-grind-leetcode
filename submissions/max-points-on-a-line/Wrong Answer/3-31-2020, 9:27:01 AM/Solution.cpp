// https://leetcode.com/problems/max-points-on-a-line

class Solution {
public:
    int maxPoints(vector<vector<int>>& points) {
        int res = 0;
        if (points.size() == 0) return 0;
        if (points.size() == 1) return 1;
        for (int i = 0; i < points.size(); i++)
            for (int j = 0; j < points.size(); j++) 
            if (i != j && points[i][0] != points[j][0] && points[i][1] != points[j][1]) {
                int cnt = 0;
                int x0 = points[i][0];
                int y0 = points[i][1];
                int x1 = points[j][0];
                int y1 = points[j][1];
                long long value = (y0 - y1) * (long long)x0 + (x1 - x0) * (long long) y0;
                for (int k = 0; k < points.size(); k++) 
                if (k != i && k != j) {
                    int x = points[k][0];
                    int y = points[k][1];
                    if ((y0 - y1) * (long long) x + (x1 - x0) * (long long) y == value) cnt++;
                }
                res = max(res, cnt + 2);
            }
        return res;
    }
};