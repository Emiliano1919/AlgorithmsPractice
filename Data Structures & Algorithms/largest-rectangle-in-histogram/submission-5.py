class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxArea = 0
        stack = []

        for i in range(n+1):
            curr_height = heights[i] if i<n else 0
            while stack and heights[stack[-1]]>curr_height:
                height=heights[stack.pop()]
                width=i-stack[-1]-1 if stack else i
                maxArea=max(maxArea,height*width)
            stack.append(i)
        return maxArea
                
                
