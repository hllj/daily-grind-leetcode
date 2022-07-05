// https://leetcode.com/problems/palindrome-number

class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0) return false;
        vector<int> d;
        while (x > 0) {
            d.push_back(x % 10);
            x /= 10;
        }
        int n = d.size();
        for(int i = 0; i < n / 2; i++) 
            if (d[i] != d[n - i - 1]) return false;
        return true;
    }
};