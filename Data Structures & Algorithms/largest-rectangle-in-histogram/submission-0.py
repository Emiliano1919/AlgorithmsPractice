class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxi=0 #FOr edge cases
        stack=[]
        for i,h in enumerate(heights):
            start=i
            while stack and stack[-1][1]>h:
                indx,height=stack.pop()
                area=height*(i-indx)
                maxi=max(area,maxi)
                start=indx
            stack.append((start,h)) #because if we pop the current rectangle can be extended back 
        while stack:
            i,h=stack.pop()
            area=h*(len(heights)-i)
            maxi=max(area,maxi)
        return maxi
