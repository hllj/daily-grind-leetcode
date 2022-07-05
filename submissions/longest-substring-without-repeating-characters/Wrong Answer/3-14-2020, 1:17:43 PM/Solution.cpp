// https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int n = s.length();
        s = "#" + s;
        
        int max_len = 0;
        for (int i = 1; i <= n; i++) {
            set <char> ss;
            bool check = 1;
            for (int j = i; j <= n; j++) {
                if (!check) break;
                ss.insert(s[j]);
                if (ss.size() == j - i + 1 && j - i + 1 > max_len) {
                    max_len = j - i + 1;
                }
                else check = 0;
            }
        }
        return max_len;
    }   
};