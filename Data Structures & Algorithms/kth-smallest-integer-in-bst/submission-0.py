# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.Counter=0
        def inorder(root):
            if not root:
                return None
            x=inorder(root.left)
            if x:
                return x
            self.Counter+=1
            if self.Counter==k:
                return root.val
            x=inorder(root.right)
            if x:
                return x
        return inorder(root)

