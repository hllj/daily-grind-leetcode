// https://leetcode.com/problems/path-sum-ii

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, u, li, s):
        if u == None:
            return
        if u.left == None and u.right == None:
            if s + u.val == self.targetSum:
                # print(u, li, s)
                self.sol.append(li + [u.val])
            return
        if s + u.val > self.targetSum:
            return
        if u.left != None:
            self.traverse(u.left, li + [u.val], s + u.val)
        if u.right != None:
            self.traverse(u.right, li + [u.val], s + u.val)
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.sol = []
        self.targetSum = targetSum
        self.traverse(root, [], 0)
        return self.sol