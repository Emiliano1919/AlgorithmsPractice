class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        maxi=0
        for i,h in enumerate(heights):
            start=i
            while stack and h<=stack[-1][1]:
                indx,height=stack.pop()
                area=(i-indx)*height
                maxi=max(area,maxi)
                start=indx
            stack.append((start,h))
        for i,h in stack:
            area=(len(heights)-i)*h
            maxi=max(area,maxi)
        return maxi
