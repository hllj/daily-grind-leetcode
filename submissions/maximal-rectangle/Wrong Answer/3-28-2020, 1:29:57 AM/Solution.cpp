// https://leetcode.com/problems/maximal-rectangle

class Solution {
public:
    int maximalRectangle(vector<vector<char>>& matrix) {
        int n = matrix.size();
        if (n == 0) return 0;
        int m = matrix[0].size();
        vector < vector<int> > f (n + 1, vector <int> (m + 1, 0));
        for (int i = 1; i <= n; i++)
            for (int j = 1; j <= m; j++) {
                f[i][j] = 0;
                if (i - 1 >= 0) f[i][j] += f[i - 1][j];
                if (j - 1 >= 0) f[i][j] += f[i][j - 1];
                if (i - 1 >= 0 && j - 1 >= 0) f[i][j] -= f[i - 1][j - 1];
                f[i][j] += (matrix[i - 1][j - 1] == '1' ? 1 : 0);
            }
        int res = 1;
        for (int i = 1; i <= n; i++)
            for (int j = 1; j <= m; j++) 
                for (int x = i; x <= n; x++)
                    for (int y = j; y <= m; y++) {
                        int sum = f[x][y] - f[x][j - 1] - f[i - 1][y] + f[i - 1][j - 1];
                        if (sum == (x - i + 1) * (y - j + 1)) {
                            res = max(res, sum);
                        }
                    }
        return res;
        
    }
};