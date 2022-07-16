// https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        root = TreeNode(val=preorder[0], left=None, right=None)
        root_idx = inorder.index(preorder[0])
        preorder_left = preorder[1: 1 + root_idx]
        preorder_right = preorder[1 + root_idx:]
        inorder_left = inorder[:root_idx]
        inorder_right = inorder[root_idx + 1:]
        left = self.buildTree(preorder_left, inorder_left)
        right = self.buildTree(preorder_right, inorder_right)
        root.left = left
        root.right = right
        return root