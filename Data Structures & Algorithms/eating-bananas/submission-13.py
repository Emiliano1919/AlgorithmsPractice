class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L=1
        R=max(piles)
        res=R
        while L<=R:
            mid=L+(R-L)//2
            totalTime=0
            for k in piles:
                totalTime+=(k+mid-1)//mid
                if totalTime>h:
                    break
            if totalTime<=h:
                res=mid
                R=mid-1
            else:
                L=mid+1
        return res