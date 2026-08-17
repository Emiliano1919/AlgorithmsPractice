"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        oldToNew={}
        oldToNew[node]= Node(node.val)
        queue = deque([node])
        while queue:
            currentNode = queue.popleft()
            for k in currentNode.neighbors:
                if k not in oldToNew:
                    oldToNew[k]=Node(k.val)
                    queue.append(k)
                oldToNew[currentNode].neighbors.append(oldToNew[k])
        return oldToNew[node]
