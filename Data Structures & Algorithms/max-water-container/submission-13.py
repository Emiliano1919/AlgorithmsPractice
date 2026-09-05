class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L=0
        R=len(heights)-1
        maxi=0
        while L<R:
            h=min(heights[L],heights[R])
            area=h*(R-L)
            maxi=max(area,maxi)
            if heights[L]<heights[R]:
                L+=1
            else:
                R-=1
        return maxi