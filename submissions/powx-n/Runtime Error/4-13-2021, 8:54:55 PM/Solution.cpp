// https://leetcode.com/problems/powx-n

class Solution {
public:
    double myPow(double x, int n) {
        if (x == 1.0) return 1;
        if (n < 0) return double(1.0) / myPow(x, n);
        if (n == 0) return 1;
        double t = myPow(x, n / 2);
        if (n % 2 == 0) return t * t;
        else return t * t * x;
    }
};