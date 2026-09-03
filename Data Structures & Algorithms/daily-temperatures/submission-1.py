class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        stack=deque()
        for i,t in enumerate(temperatures):
            while stack and t>stack[-1][1]:
                prvIdx,_=stack.pop()
                res[prvIdx]=i-prvIdx
            stack.append((i,t))
        return res