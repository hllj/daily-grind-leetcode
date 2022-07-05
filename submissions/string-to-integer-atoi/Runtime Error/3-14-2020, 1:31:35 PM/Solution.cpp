// https://leetcode.com/problems/string-to-integer-atoi

class Solution {
public:
    int myAtoi(string str) {
        if (str[0] >= 'a' && str[0] <= 'z') return 0;
        int idx = 0;
        while (idx < str.length()) {
            if (str[idx] >= 'a' && str[idx] <= 'z') {
                str.erase(idx, 1);
                idx--;
            }
            idx++;
        }
        while (str[0] == ' ') 
            str.erase(0, 1);
        while (str[str.length() - 1] == ' ')
            str.erase(str.length() - 1, 1);
        int sign = 1;
        if (str[0] == '-') {
            sign = -1;
            str.erase(0, 1);
        }
        int value = 0;
        for (int i = 0; i < str.length(); i++)
            value = (int) value * (int) 10 + (str[i] - '0');
        return value * sign;
    }
};