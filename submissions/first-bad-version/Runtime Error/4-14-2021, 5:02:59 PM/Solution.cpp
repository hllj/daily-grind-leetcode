// https://leetcode.com/problems/first-bad-version

// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        double left = 1;
        double right = n;
        int i = (int) (left + right) / 2;
        while(left != i && i != right) {
            if (isBadVersion(i) == true) right = i;
            else left = i;
            i =  (int) (left + right) / 2;
        }
        for(int x=left; x <= right; x++) 
            if (isBadVersion(x) == true) return x;
        return -1;
    }
};