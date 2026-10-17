class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft=height[0]
        maxRight=height[-1]
        L=1
        R=len(height)-2
        res=0
        while L<=R:
            if maxLeft<maxRight:
                maxLeft=max(maxLeft,height[L])
                res+=maxLeft-height[L]
                L+=1
            else:
                maxRight=max(maxRight,height[R])
                res+=maxRight-height[R]
                R-=1
        return res