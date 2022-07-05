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
        else f[i][j] = 0;
  for (int i = 1; i <= n; i++) 
    for (int j = i - 1; j >= 1; j--)
      if (s[i] == s[j]) f[j][i] = f[j + 1][i - 1] + 2;
        else f[j][i] = max(f[j + 1][i], f[j][i - 1]);
  int x = 1, y = n;
  string res = "";
  while (x <= y) {
    cout << x << " " << y << "\n";
    if (s[x] == s[y]) {
      string temp = "";
      if (x == y) {
        temp = temp + s[x];
      }
      else {
        temp = temp + s[x] + s[y];
      }
      res.insert(res.length() / 2, temp);
      x++;
      y--;
    }
    else {
      if (f[x][y] == f[x + 1][y]) x++;
      else y--;
    }
  }
  return res;
        
    }
};