// https://leetcode.com/problems/longest-valid-parentheses

class Solution {
public:
    int longestValidParentheses(string s) {
        int res = 0;
        stack <char> st;
        for (int i = 0l; i < s.length(); i++) {
            if (s[i] == '(') st.push(s[i]);
            else {
                if (st.top() == '(') st.pop(), res += 2;
            }
        }
        return res;
    }
};