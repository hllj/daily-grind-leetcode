// https://leetcode.com/problems/decode-ways

class Solution {
public:
    int numDecodings(string s) {
        int n = s.length();
        vector<int> f(n + 5, 0);
        if (s[0] == '0') return 0;
        f[0] = 1;
        for(int i = 1; i <= n; i++) {
            f[i] = 0;
            if (s[i - 1] >= '1' && s[i - 1] <= '9') f[i] += f[i - 1];
            if (i >= 2) {
                string d = "";
                d = d + s[i - 2] + s[i - 1];
                if (d >= "1" && d <= "26") f[i] += f[i - 2];
            }
        }
        return f[n];
    }
};