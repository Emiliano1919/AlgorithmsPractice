class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        res=[0]*len(temperatures)
        for day,t in enumerate(temperatures):
            while stack and stack[-1][0]<t:
                _,prevDay=stack.pop()
                res[prevDay]=day-prevDay
            stack.append((t,day))
        return res
