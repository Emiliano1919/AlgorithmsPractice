# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.count=0
        def helper(root,targetSum):
            if not root:
                return False
            self.count+=root.val
            if not root.left and not root.right:
                if self.count==targetSum:
                    return True
            if root.left and helper(root.left,targetSum):
                return True
            if root.right and helper(root.right,targetSum):
                return True
            self.count-=root.val
            return False
        return helper(root,targetSum)
    