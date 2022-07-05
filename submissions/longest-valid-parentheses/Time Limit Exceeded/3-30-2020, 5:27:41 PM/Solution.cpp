// https://leetcode.com/problems/longest-valid-parentheses

class Solution {
public:
    int longestValidParentheses(string s) {
        int res = 0;
        int n = s.length();
        stack <char> temp;
        stack <char> st;
        for (int i = 0; i < n; i++) {
            int j = i;
            while (j < n) {
                if (s[j] == '(') st.push(s[j]);
                else {
                    if (!st.empty() && st.top() == '(') st.pop();
                    else st.push(s[j]);
                }
                if (st.empty()) {
                    res = max(res, j - i + 1);
                }
                j++;
            }
            st = temp;
        }
        return res;
    }
};