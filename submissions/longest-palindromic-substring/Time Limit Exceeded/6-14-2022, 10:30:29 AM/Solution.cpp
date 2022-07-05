// https://leetcode.com/problems/longest-palindromic-substring

class Solution {
public:
    string longestPalindrome(string s) {
        int n = s.length();
  s = "#" + s;
  vector < vector<int> > f (n + 1);
  for (int i = 0; i <= n; i++) 
    for (int j = 0; j <= n; j++)
      f[i].push_back(0);
  for (int i = 1; i <= n; i++)
    for (int j = 1; j <= n; j++)
      if (i == j) f[i][j] = 1;
        else {
          if (i > j) f[i][j] = 1;
          else f[i][j] = 0;
        }
  
  for (int i = 1; i <= n; i++) 
    for (int j = i - 1; j >= 1; j--)
      if (s[j] == s[i]) f[j][i] = f[j + 1][i - 1];
        else f[j][i] = 0;

  int max_len = 0;
  int max_i = -1;
  int max_j = -1;
  for (int i = 1; i <= n; i++)
    for (int j = i; j <= n; j++)
      if (f[i][j]) {
        if (j - i + 1 > max_len) {
          max_len = j - i + 1;
          max_i = i;
          max_j = j;
        }
      }
  if (max_len == 0) return "";
  else
    return s.substr(max_i, max_j - max_i + 1);
        
    }
};