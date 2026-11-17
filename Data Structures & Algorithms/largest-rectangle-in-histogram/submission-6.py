class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        res=0
        for i in range(len(heights)+1):
            curr_h = 0 if i == len(heights) else heights[i]
            while stack and heights[stack[-1]]>=curr_h:
                oldIdx=stack.pop()
                width=i-stack[-1]-1 if stack else i
                res=max(width*heights[oldIdx],res)
            stack.append(i)

        return res