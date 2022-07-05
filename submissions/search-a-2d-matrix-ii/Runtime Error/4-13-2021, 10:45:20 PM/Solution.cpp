// https://leetcode.com/problems/search-a-2d-matrix-ii

class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int m = matrix.size();
        int n = matrix[0].size();
        if (target < matrix[0][0] || target > matrix[m - 1][n - 1]) return false;
        int left = 0, right = m - 1;
        while (left < right) {
            int mid = (left + right) >> 1;
            if (matrix[mid][0] == target) return true;
            else if (matrix[mid][0] < target) left = mid + 1;
            else right = mid - 1;
        }
        if (left == right && matrix[left][0] == target) return true;
        
        int s1 = right;
        left = 0, right = n - 1;
        while (left < right) {
            int mid = (left + right) >> 1;
            if (matrix[s1][mid] == target) return true;
            else if (matrix[s1][mid] < target) left = mid + 1;
            else right = mid - 1;
        }
        if (left == right && matrix[s1][left] == target) return true;
        int s2 = right;
        left = 0, right = m - 1;
        while (left < right) {
            int mid = (left + right) >> 1;
            if (matrix[mid][s2] == target) return true;
            else if (matrix[mid][s2] < target) left = mid + 1;
            else right = mid - 1;
        }
        if (left == right && matrix[left][s2] == target) return true;
        return false;
    }
};