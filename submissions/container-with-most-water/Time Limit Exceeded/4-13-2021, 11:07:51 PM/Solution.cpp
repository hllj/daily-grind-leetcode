// https://leetcode.com/problems/container-with-most-water

class Solution {
public:
    int maxArea(vector<int>& height) {
        int n = height.size();
        int ret = 0;
        for(int i = 0; i < n; i++) 
            for(int j = i + 1; j < n; j++)
                ret = max(ret, min(height[i], height[j]) * (j - i));
        return ret;
    }
};