// https://leetcode.com/problems/first-bad-version

// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        int left = 1;
        int right = n;
        int i =(left >> 1) + (right >> 1);
        while(left != i && i != right) {
            if (isBadVersion(i) == true) right = i;
            else left = i;
            i = (left >> 1) + (right >> 1);
        }
        for(int x=left; x <= right; x++) 
            if (isBadVersion(x) == true) return x;
        return -1;
    }
};