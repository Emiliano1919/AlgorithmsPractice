# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        if not root:
            return res
        que=deque()
        que.append(root)
        while len(que)>0:
            res.append(que[0].val)
            for _ in range(len(que)):
                curr=que.popleft()
                if curr.right:
                    que.append(curr.right)
                if curr.left:
                    que.append(curr.left) 
            
        return res