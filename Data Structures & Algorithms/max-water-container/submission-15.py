class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L=0
        R=len(heights)-1
        res=0
        while L<R:
            if heights[L]<heights[R]:
                res=max(heights[L]*(R-L),res)
                L+=1
            else:
                res=max(heights[R]*(R-L),res)
                R-=1
        return res
