class Solution:
    def trap(self, height: List[int]) -> int:
        i=1
        j=len(height)-2
        maxLeft=height[0]
        maxRight=height[len(height)-1]
        res=0
        while i<=j:#Because we need to process both the invariant here is that i and j represent unprocessed.
        #If i lands in j but j is unprocessed we need this condition to process it
        #Remember to think about what things represent
            if maxLeft<maxRight:
                maxLeft=max(maxLeft,height[i])
                res+=maxLeft-height[i]
                i+=1
            else:
                maxRight=max(maxRight,height[j])
                res+=maxRight-height[j]
                j-=1
        return res
