# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val<key:
            root.right=self.deleteNode(root.right,key)
        elif root.val>key:
            root.left=self.deleteNode(root.left,key)
        else:
            if not root.right: 
                # This handle the case of not having children and also of just having the left child
                return root.left
            elif not root.left:
                return root.right
            else:
                minNode=self.minValue(root.right)
                root.val=minNode.val
                #To delete again we only need to search on right subtree
                #Even if we have already put the minNode by searching just the right we dont delete the one we just put
                root.right=self.deleteNode(root.right,minNode.val)
        return root

    def minValue(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        curr = root
        while curr and curr.left: #Important to keep the curr one because if not you delete the node
            curr = curr.left
        return curr
        