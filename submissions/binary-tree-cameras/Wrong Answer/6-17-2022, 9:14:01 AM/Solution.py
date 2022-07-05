// https://leetcode.com/problems/binary-tree-cameras

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def dfs(self, u, i):
        if u == None:
            return 0
        if i == 0:
            return self.dfs(u.left, 1) + self.dfs(u.right, 1)
        else:
            return 1 + self.dfs(u.left, 0) + self.dfs(u.right, 0)
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        ans1 = self.dfs(root, 0)
        ans2 = self.dfs(root, 1)
        return max(1, min(ans1, ans2))