// https://leetcode.com/problems/valid-palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new_s = ''
        for x in s:
            if (ord('0') <= ord(x) <= ord('9')) or (ord('a') <= ord(x) <= ord('z')) or (ord('A') <= ord(x) <= ord('Z')):
                new_s += x
        print(new_s)
        n = len(new_s)
        for i in range(n // 2):
            if new_s[i] != new_s[n - i - 1]:
                return False
        return True