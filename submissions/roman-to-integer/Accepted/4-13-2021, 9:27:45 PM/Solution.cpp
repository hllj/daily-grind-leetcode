// https://leetcode.com/problems/roman-to-integer

class Solution {
public:
    int romanToInt(string s) {
        vector<int> trans;
        for(int i = 0; i < s.length(); i++) {
            if (s[i] == 'I') trans.push_back(1);
            if (s[i] == 'V') trans.push_back(5);
            if (s[i] == 'X') trans.push_back(10);
            if (s[i] == 'L') trans.push_back(50);
            if (s[i] == 'C') trans.push_back(100);
            if (s[i] == 'D') trans.push_back(500);
            if (s[i] == 'M') trans.push_back(1000);
        }
        int ret = 0;
        for (int i = 0; i < trans.size(); ) {
            if (i == trans.size() - 1) {
                ret += trans[i];
                break;
            }
            if (trans[i] < trans[i + 1]) {
                ret += trans[i + 1] - trans[i];
                i += 2;
            } else {
                ret += trans[i];
                i += 1;
            }
        }
        return ret;
    }
};