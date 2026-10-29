class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L=1
        R=max(piles)
        res=math.inf
        while L<=R:
            mid=L+(R-L)//2
            time=0
            for p in piles:
                time+=math.ceil(p/mid)
                if time>h:
                    break
            if time>h:
                L=mid+1
            else:
                R=mid-1
        return L