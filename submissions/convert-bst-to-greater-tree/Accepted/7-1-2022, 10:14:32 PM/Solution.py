// https://leetcode.com/problems/convert-bst-to-greater-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, u, parent_sum):
        if u is None:
            return None, parent_sum
        r, parent_sum = self.traverse(u.right, parent_sum)
        parent_sum += u.val
        u.val = parent_sum
        l, parent_sum = self.traverse(u.left, parent_sum)
        return u, parent_sum
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        root, parent_sum = self.traverse(root, 0)
        return root