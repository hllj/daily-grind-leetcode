// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    candidates = []
    candidates_value = []
    cnt_descendant = {}
    def descendant(self, d, p):
        if d == None:
            return False
        if d.val == p.val:
            if p.val not in self.cnt_descendant:
                self.cnt_descendant[d.val] = 1
            else:
                self.cnt_descendant[d.val] += 1
            return True
        else:
            is_descendant = self.descendant(d.left, p) or self.descendant(d.right, p)
            if d.val not in self.cnt_descendant:
                self.cnt_descendant[d.val] = 0
            if is_descendant is True:
                self.cnt_descendant[d.val] += 1
            return is_descendant
    def search(self, p):
        if p == None:
            return
        if p.val not in self.cnt_descendant:
            return
        if self.cnt_descendant[p.val] == 2:
            self.candidates.append(p)
            self.candidates_value.append(p.val)
        
        if p.left != None:
            self.search(p.left)
        if p.right != None:
            self.search(p.right)
            
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.descendant(root, p)
        self.descendant(root, q)
        print(self.cnt_descendant)
        self.search(root)
        print(self.candidates_value)
        return self.candidates[-1]