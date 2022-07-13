// https://leetcode.com/problems/binary-tree-level-order-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, u, level):
        if u == None:
            return
        if level not in self.order:
            self.order[level] = []
        self.order[level].append(u.val)
        self.traverse(u.left, level + 1)
        self.traverse(u.right, level + 1)
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.order = {}
        res = []
        self.traverse(root, 0)
        if len(self.order) == 0:
            return []
        for i in range(max(self.order.keys()) + 1):
            res.append(self.order[i])
        return res
        