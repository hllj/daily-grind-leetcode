// https://leetcode.com/problems/palindrome-pairs

class Solution {
public:
    vector<vector<int>> palindromePairs(vector<string>& words) {
        vector < vector <int> > res;
        for (int i = 0; i < words.size(); i++) 
            for (int j = i + 1; j < words.size(); j++) {
                if (isPalin(words[i] + words[j])) {
                    vector <int> v{i, j};
                    res.push_back(v);
                }
                if (isPalin(words[j] + words[i])) {
                    vector <int> v{j, i};
                    res.push_back(v);
                }
            }
        return res;
    }
    bool isPalin(string s) {
        int i = 0, j = s.length() - 1;
        while (i < j) {
            if (s[i] != s[j]) return false;
            i++;
            j--;
        }
        return true;
    }
};