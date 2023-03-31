# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p1 = []
        p2 = []

        def rec(r, target, path):
            path.append(r)
            if target == r:
                return
            elif target.val > r.val:
                rec(r.right, target, path)
            else:
                rec(r.left, target, path)
        rec(root, p, p1)
        rec(root, q, p2)
        #print(p1, p2)
        M = min(len(p1), len(p2))
        for i in range(M):
            if p1[i] != p2[i]:
                return p1[i-1]
        return p1[M-1]
        return root