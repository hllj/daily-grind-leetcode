// https://leetcode.com/problems/number-of-distinct-roll-sequences

using namespace std;

class Solution {
public:
    int distinctSequences(int n) {
        if (n == 1) return 6;
        if (n == 2) return 22;
        long long modulo = 1e9 + 7;
        long long f[n + 1][6][6];
        for (int j = 0; j < 6; j++)
            for (int k = 0; k < 6; k++) {
                f[2][j][k] = 0;
                if (__gcd(j + 1, k + 1) == 1 && j != k)
                    f[2][j][k] = 1;
            }
        long long res = 0;
        for (int i = 3; i <= n; i++)
            for (int j = 0; j < 6; j++)
                for (int k = 0; k < 6; k++) {
                    f[i][j][k] = 0;
                    for (int j0 = 0; j0 < 6; j0++)
                        if (__gcd(j + 1, k + 1) == 1 && j != k && j0 != k && (__gcd(j0 + 1, j + 1) == 1))
                            f[i][j][k] = (f[i][j][k] + f[i - 1][j0][j]) % modulo;
                    if (i == n)
                        res = (res + f[i][j][k]) % modulo;
                }
        return res;
    }
};