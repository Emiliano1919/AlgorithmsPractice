class Solution:
    def trap(self, height: List[int]) -> int:
        i=1
        j=len(height)-2
        maxLeft=height[0]
        maxRight=height[len(height)-1]
        res=0
        while i<=j:
            maxLeft=max(maxLeft,height[i])
            maxRight=max(maxRight,height[j])
            if maxLeft<maxRight:
                res+=maxLeft-height[i]
                i+=1
            else:
                res+=maxRight-height[j]
                j-=1
        return res
