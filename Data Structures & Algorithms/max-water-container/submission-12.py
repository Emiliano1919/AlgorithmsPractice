class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxA=0
        i=0
        j=len(heights)-1
        while i<j:
            curr=(j-i)*min(heights[i],heights[j])
            maxA=max(curr,maxA)
            if heights[i]<heights[j]:
                i+=1
            elif heights[j]<heights[i]:
                j-=1
            else:
                i+=1
                j-=1
        return maxA
