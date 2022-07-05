// https://leetcode.com/problems/edit-distance

class Solution {
public:
    int minDistance(string word1, string word2) {
        int n1 = word1.length();
        int n2 = word2.length();
        word1 = "#" + word1;
        word2 = "#" + word2;
        vector < vector<int> > f (n1 + 1, vector<int> (n2 + 1));
        for (int i = 0; i <= n1; i++)
            for (int j = 0; j <= n2; j++)
                f[i][j] = 0;
        for (int i = 0; i <= n1; i++)
            f[i][0] = i;
        for (int j = 0; j <= n2; j++)
            f[0][j] = j;
        for (int i = 1; i <= n1; i++)
            for (int j = 1; j <= n2; j++)
                if (word1[i] != word2[j]) {
                    f[i][j] = min(min(f[i - 1][j], f[i][j - 1]), f[i - 1][j - 1]) + 1;
                }
                else f[i][j] = f[i - 1][j - 1];
        return f[n1][n2];
    }
};