// https://leetcode.com/problems/sum-root-to-leaf-numbers

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = 0
    def traverse(self, p, s):
        if p == None:
            return 0
        s = s * 10 + p.val
        if (p.left == None and p.right == None):
            self.res += s
        self.traverse(p.left, s * 10)
        self.traverse(p.right, s * 10)
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.traverse(root, root.val)
        return self.res