class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        q=deque()
        res=[0]*len(temperatures)
        for i,t in enumerate(temperatures):
            while q and t>q[-1][1]:
                old=q.pop()[0]
                res[old]=i-old
            q.append((i,t))
        return res
