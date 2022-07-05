// https://leetcode.com/problems/powx-n

class Solution {
public:
    double myPow(double x, int n) {
        double a;
        if(n<0){
            double b=-1;
            b=b*n;
            double c;
            c=pow(x,b);
            double d;
            d=1/c;
            return d;
        }
        a=pow(x,n);
        return a;
    }
};