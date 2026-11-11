class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L=1
        R=max(piles)
        res=R
        while L<=R:
            m=L+(R-L)//2
            cT=0
            for p in piles:
                cT+=math.ceil(p/m)
                if cT>h:
                    break
            if cT>h:
                L=m+1
            else:
               res=m
               R=m-1
        return res
