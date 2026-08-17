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
        oldToNew = {}
        def dfs(nd):
            if nd in oldToNew:
                return oldToNew[nd]
            copy = Node(nd.val)
            oldToNew[nd] = copy
            for k in nd.neighbors:
                copy.neighbors.append(dfs(k))
            return copy
        return dfs(node)