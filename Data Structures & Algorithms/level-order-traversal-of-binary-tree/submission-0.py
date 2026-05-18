# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        mainList=[]
        if not root:
            return mainList
        que=deque()
        que.append(root)
        while len(que)>0:
            levelList=[]
            for _ in range(len(que)):
                curr=que.popleft()
                levelList.append(curr.val)
                if curr.left:
                    que.append(curr.left)
                if curr.right:
                    que.append(curr.right)
            mainList.append(levelList)
        return mainList