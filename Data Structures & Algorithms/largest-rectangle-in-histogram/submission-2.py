class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        maxArea = 0
        stack=[]

        for i in range(n+1):
            #We are doing it till n inclusive because we need to count till we are at the very end
            while stack and (i==n or heights[stack[-1]] >= heights[i]):
                #If we are not in a monotonic state calculate
                height = heights[stack.pop()]
                #Notice you pop the height but you keep something in the stack (we are keeping the last known invalid position use to calculate the width thats why we reduce by 1 because we are overcounting)
                width = i if not stack else i-stack[-1]-1
                maxArea = max(maxArea,height * width)
            stack.append(i)
        return maxArea
