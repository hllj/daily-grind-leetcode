// https://leetcode.com/problems/binary-tree-right-side-view

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        left = self.rightSideView(root.left)
        right = self.rightSideView(root.right)
        if len(left) > len(right):
            return [root.val] + right + left[len(right):]
        else:
            return [root.val] + right