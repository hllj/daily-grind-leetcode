// https://leetcode.com/problems/search-a-2d-matrix-ii

class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int n = matrix.size();
        int m = matrix[0].size();
        if (target < matrix[0][0] || target > matrix[n - 1][m - 1]) return false;
        for(int i = 0; i < n; i++)
            if (target >= matrix[i][0] && target <= matrix[i][m - 1]) {
                int left = 0, right = m - 1;
                while (left < right) {
                    int mid = (left + right) >> 1;
                    if (matrix[i][mid] == target) return true;
                    if (matrix[i][mid] > target) right = mid - 1;
                    else left = mid + 1;
                }
                if (matrix[i][left] == target) return true;
            } else return false;
        return false;
    }
};