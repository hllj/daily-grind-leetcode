// https://leetcode.com/problems/first-bad-version

// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        int left = 1;
        int right = n;
        while (left < right) {
            int mid = (left + right) >> 1;
            if (isBadVersion(mid) == true) right = mid - 1;
            else left = mid + 1;
        }
        return left;
    }
};