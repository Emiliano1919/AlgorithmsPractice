class Solution:
    def trap(self, height: List[int]) -> int:
        res=0
        L=0
        R=len(height)-1
        maxLeft,maxRight=height[L],height[R]
        res=0
        while L<R:
            if maxLeft<maxRight:
                L+=1
                res+=max(0, maxLeft-height[L])
                maxLeft=max(maxLeft,height[L])
            else:
                R-=1
                res+=max(0, maxRight-height[R])
                maxRight=max(maxRight,height[R])
        return res