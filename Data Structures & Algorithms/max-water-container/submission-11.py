class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxA=0
        i=0
        j=len(heights)-1
        while i<j:
            curr=(j-i)*min(heights[i],heights[j]) if i!=0 else (j)*min(heights[i],heights[j])
            if curr>maxA:
                maxA=curr
            if heights[i]<heights[j]:
                i+=1
                continue
            elif  heights[j]<heights[i]:
                j-=1
                continue
            else:
                i+=1
                j-=1
                continue
            
        return maxA
            
        