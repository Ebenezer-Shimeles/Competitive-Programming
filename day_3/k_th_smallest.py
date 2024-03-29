# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        nums = []

        def rec_add(root):

            if not root:
                return
            rec_add(root.left)
            nums.append(root.val)
            rec_add(root.right)
        rec_add(root)
        return nums[k-1]