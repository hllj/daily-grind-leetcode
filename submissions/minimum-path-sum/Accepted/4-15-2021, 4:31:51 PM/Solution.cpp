// https://leetcode.com/problems/minimum-path-sum

class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        vector< vector<int> > f (m + 5, vector<int> (n + 5, 0));
        f[0][0] = grid[0][0];
        for(int i = 1; i < m; i++)
            f[i][0] = f[i - 1][0] + grid[i][0];
        for(int j = 1; j < n; j++)
            f[0][j] = f[0][j - 1] + grid[0][j];
        for(int i = 1; i < m; i++) {
            for(int j = 1; j < n; j++) {
                f[i][j] = min(f[i - 1][j], f[i][j - 1]) + grid[i][j];
            }
        }
        return f[m - 1][n - 1];
    }
};