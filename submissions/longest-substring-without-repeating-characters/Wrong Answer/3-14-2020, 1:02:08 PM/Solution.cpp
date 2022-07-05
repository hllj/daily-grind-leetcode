// https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int n = s.length();
        s = "#" + s;
        vector < vector<int> > cnt(26);
        for (int t = 0; t < 26; t++) {
            for (int i = 0; i <= n; i++)
                cnt[t].push_back(0);
            for (int i = 1; i <= n; i++) {
                cnt[t][i] = cnt[t][i - 1];
                if (s[i] == 'a' + t) cnt[t][i]++;
            }
        }
        
        int max_len = 0;
        int max_i = -1;
        int max_j = -1;
        for (int i = 1; i <= n; i++)
            for (int j = i; j <= n; j++) {
                bool check = 1;
                for (int t = 0; t < 26; t++) {
                    int cnt_t = cnt[t][j] - cnt[t][i - 1];
                    if (!(cnt_t == 1 || cnt_t == 0)) check = 0;
                }
                if (check && j - i + 1 > max_len) {
                    max_len = j - i + 1;
                    max_i = i;
                    max_j = j;
                }
            }
        return max_len;
    }   
};