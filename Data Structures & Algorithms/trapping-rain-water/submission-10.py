class Solution:
    def trap(self, height: List[int]) -> int:
        L=0
        R=len(height)-1
        maxLeft,maxRight=height[L],height[R]
        res=0
        while L<R:
            if maxLeft<maxRight:
                L+=1
                maxLeft=max(maxLeft,height[L])
                res+=maxLeft-height[L]
            else:
                R-=1
                maxRight=max(maxRight,height[R])
                res+=maxRight-height[R]
        return res
            