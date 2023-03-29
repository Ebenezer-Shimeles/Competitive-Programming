# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        # L Rt R
        return_value = []

        r = root
        if not r:
            return []
        stack.append(r)
        while r.left:
            stack.append(r.left)
            r = r.left
        while len(stack):
            t = stack.pop()
            return_value.append(t.val)
            if t.right:
                # stack.append(t.right)
                r = t.right
                stack.append(r)
                while r.left:
                    stack.append(r.left)
                    r = r.left
        return return_value

        
        