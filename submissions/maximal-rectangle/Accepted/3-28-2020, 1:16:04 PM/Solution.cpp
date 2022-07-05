// https://leetcode.com/problems/maximal-rectangle

class Solution {
public:
    int maximalRectangle(vector<vector<char>>& matrix) {
        if(matrix.empty()) return 0;
        const int m = matrix.size(), n = matrix[0].size();
        int area = 0;
        vector<vector<int>> dp(m, vector<int>(n + 1, 0));
        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                if(!i) dp[i][j] = matrix[i][j] - '0';
                else if(matrix[i][j] - '0') dp[i][j] = dp[i - 1][j] + 1;
                else dp[i][j] = 0;
            }
        }
        for(int j = 0; j < m; j++) {
            stack<int> s;
            int i = 0;
            while(i <= n) {
                if(s.empty() || dp[j][i] >= dp[j][s.top()]) s.push(i++);
                else {
                    int cur = s.top(); s.pop();
                    area = max(area, dp[j][cur] * (s.empty() ? i : i - s.top() - 1));
                }
            }
        }
        return area;
        
    }
};