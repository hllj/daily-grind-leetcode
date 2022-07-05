// https://leetcode.com/problems/deepest-leaves-sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    height = 0
    res = 0
    def traverse(self, p, h):
        if p == None:
            return
        p.height = h
        self.height = max(self.height, h)
        self.traverse(p.left, h + 1)
        self.traverse(p.right, h + 1)
    
    def searchDeepestNode(self, p):
        if p == None:
            return
        if p.height == self.height:
            self.res += p.val
        self.searchDeepestNode(p.left)
        self.searchDeepestNode(p.right)
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:   
        self.height = 0
        self.res = 0
        self.traverse(root, 0)
        self.searchDeepestNode(root)
        return self.res
                
        