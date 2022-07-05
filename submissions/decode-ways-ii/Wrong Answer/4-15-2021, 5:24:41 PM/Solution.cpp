// https://leetcode.com/problems/decode-ways-ii

class Solution {
public:
    int numDecodings(string s) {
        int n = s.length();
        int modulo = 1e9 + 7;
        vector<int> f(n + 5, 0);
        if (s[0] == '0') return 0;
        f[0] = 0;
        for(int i = 1; i <= n; i++) {
            f[i] = 0;
            if (s[i - 1] >= '1' && s[i - 1] <= '9') f[i] = (f[i] + f[i - 1]) % modulo;
            else if (s[i - 1] == '*') f[i] = (f[i - 1] + 9) % modulo;
            //cout << "check 1:" << f[i] << "\n";
            if (i >= 2) {
                string d = "";
                d = d + s[i - 2] + s[i - 1];
                if (d[0] != '*' && d[1] != '*' && d >= "1" && d <= "26") { 
                    f[i] = (f[i] + f[i - 2]) % modulo;
                }
                else {
                    int cnt = 0;
                    string tmp;
                    tmp = d;
                    if (d == "**") f[i] = (f[i] + f[i - 2] + 26) % modulo;
                    if (d[0] == '*' && d[1] != '*') 
                        for(char c='1'; c <= '9'; c++) {
                            tmp[0] = c;
                            if (tmp >= "1" && tmp <= "26") cnt++;
                        }
                    tmp = d;
                    if (d[1] == '*' && d[0] != '*') 
                        for(char c='1'; c <= '9'; c++) {
                            tmp[1] = c;
                            if (tmp >= "1" && tmp <= "26") cnt++;
                        }
                    f[i] = (f[i] + f[i - 2] + cnt) % modulo;
                    //cout << "check 2:" << cnt << "\n";
                }
            }
        }
        return f[n];
    }
};