# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def rec(r):
            if r == None:
                return None
            
            ri = rec(r.right)
            le = rec(r.left)

            if ri == False or le == False:
                return False
            if not ri and not le:
                return r.val
            elif not ri:
                if r.val <= le:
                    return False
                return r.val
            elif not le:
                if r.val >= ri:
                    return False
                return  ri
            else:
                if le >= r.val or ri <= r.val:
                    return False
                else:
                    return ri
            

        return rec(root)