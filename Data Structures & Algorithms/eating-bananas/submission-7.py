class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L=1 #We cannot go lower than this because??
        R=max(piles)
        minim=R
        while L<=R:
            mid=L+(R-L)//2
            curr=0
            for x in piles:
                curr+=(x+mid-1)//mid
            if curr<=h:
                minim=mid
                R=mid-1
            else: #curr>h
                L=mid+1
        return minim