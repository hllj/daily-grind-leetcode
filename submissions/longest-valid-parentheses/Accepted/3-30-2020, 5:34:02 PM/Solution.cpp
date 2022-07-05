// https://leetcode.com/problems/longest-valid-parentheses

class Solution {
public:
    int longestValidParentheses(string s) {
        stack<int> st;
        int current_length = 0,max_length = 0;
        st.push(-1);
        for(int i=0;i<s.size();i++)
        {
            if(s[i]=='(')
            {
                st.push(i);
            }
            else
            {
                st.pop();
                if(st.size()==0)
                {
                    st.push(i);
                }
                else
                {
                    current_length = i-st.top();
                    max_length = max(current_length,max_length);
                }
            }
        }
        return max_length;
    }
};