// https://leetcode.com/problems/unique-paths

class Solution {
public:
    int uniquePaths(int m, int n) {
        vector< vector<int> > f (m + 5, vector<int> (n + 5, 1));
        f[1][1] = 0;
        for(int j = 1; j <= n; j++) f[1][j] = 1;
        for(int i = 1; i <= m; i++) f[i][1] = 1;
        for(int i = 2; i <= m; i++)
            for(int j = 2; j <= n; j++) {
                f[i][j] = f[i - 1][j] + f[i][j - 1];
            }
        return f[m][n];
    }
};