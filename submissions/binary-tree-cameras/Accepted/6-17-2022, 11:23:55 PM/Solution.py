// https://leetcode.com/problems/binary-tree-cameras

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, par=None):
        if node:
            self.dfs(node.left, node)
            self.dfs(node.right, node)
            if (par is None and node not in self.covered or node.left not in self.covered or node.right not in self.covered):
                self.ans += 1
                self.covered.update({node, par, node.left, node.right})
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.covered = {None}
        self.dfs(root)
        return self.ans