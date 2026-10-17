class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L=1
        R=max(piles)
        res=R
        while L<=R:
            mid=L+(R-L)//2
            total=0
            for k in piles:
                total+=(k+mid-1)//mid
                if total>h:
                    break
            if total<=h:
                res=mid
                R=mid-1
            else:
                L=mid+1
        return res