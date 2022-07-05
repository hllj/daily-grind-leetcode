// https://leetcode.com/problems/count-numbers-with-unique-digits

class Solution {
public:
    int countNumbersWithUniqueDigits(int n) {
        if (n == 0) return 1;
        int res = 10;
        int prev = 10;
        for(int i = 1; i < n; i++) {
            if (i == 1) prev--;
            int cnt = prev * (10 - i);
            res += cnt;
            prev = cnt;
        }
        return res;
    }
};