
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        N = len(preorder)

        if not N:
            return None
        if N== 1:
            return TreeNode(val=preorder[0])
        inorder = sorted(preorder)
        root_val = preorder[0]
        root_index = inorder.index(root_val)
        left_preorder = preorder[1:1+root_index]
        right_preorder = preorder[1+root_index:]
        print(left_preorder, right_preorder)
        root = ListNode(val = root_val)
        root.right = self.bstFromPreorder(right_preorder)
        root.left = self.bstFromPreorder(left_preorder)
        return root


