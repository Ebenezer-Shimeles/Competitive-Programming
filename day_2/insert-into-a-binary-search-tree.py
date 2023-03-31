# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        to_be_inserted = TreeNode(val = val)
        if not root:
            return to_be_inserted
        r = root

        while True:
            if r.val > val:
                
                if r.left:
                    r = r.left
                else:
                    r.left = to_be_inserted
                    return root
            else:
                if r.right:
                    r = r.right
                else:
                    r.right = to_be_inserted
                    return root

            