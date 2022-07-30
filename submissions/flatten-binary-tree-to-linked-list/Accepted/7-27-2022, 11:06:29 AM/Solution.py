// https://leetcode.com/problems/flatten-binary-tree-to-linked-list

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root == None:
            return None, None
        left, right = root.left, root.right
        modified_left, right_left = self.flatten(left)
        # print('left', modified_left, right_left)
        modified_right, right_right = self.flatten(right)
        # print('right', modified_right, right_right)
        root.left = None
        root.right = modified_left
        if modified_left != None:
            right_left.right = modified_right
        else:
            root.right = modified_right
        
        if left == None and right == None:
            return root, root
        if right != None:
            return root, right_right
        if left != None:
            return root, right_left