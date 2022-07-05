// https://leetcode.com/problems/longest-valid-parentheses

class Solution {
public:
    int longestValidParentheses(string s) {
        int res = 0;
        int n = s.length();
        stack <char> st;
        st.push(-1);
        for (int i = 0; i < n; i++) {
            if (s[i] == '(') {
                st.push(i);
            }
            else {
                st.pop();
                if (st.size() == 0) {
                    st.push(i);
                }
                else {
                    res = max(res, i - st.top());
                }
            }
        }
            
        return res;
    }
};