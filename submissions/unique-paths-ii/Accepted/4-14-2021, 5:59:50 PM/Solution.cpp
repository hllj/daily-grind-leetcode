// https://leetcode.com/problems/unique-paths-ii

class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int m = obstacleGrid.size();
        int n = obstacleGrid[0].size();
        vector< vector<int> > f (m + 5, vector<int> (n + 5, 1));
        f[1][1] = 0;
        for(int j = 1; j <= n; j++) 
            if (obstacleGrid[0][j - 1] == 0) f[1][j] = f[1][j - 1];
            else f[1][j] = 0;
        for(int i = 1; i <= m; i++) 
            if (obstacleGrid[i - 1][0] == 0) f[i][1] = f[i - 1][1];
            else f[i][1] = 0;
        for(int i = 2; i <= m; i++)
            for(int j = 2; j <= n; j++) 
            if (obstacleGrid[i - 1][j - 1] == 0) {
                f[i][j] = f[i - 1][j] + f[i][j - 1];
            }
            else f[i][j] = 0;
        return f[m][n];
    }
};