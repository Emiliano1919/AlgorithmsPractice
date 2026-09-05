class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L=1 #We cannot go lower than this because, YOU CANNOT DO Eating at rate 0
        R=max(piles)
        minim=R
        while L<=R:
            mid=L+(R-L)//2
            curr=0
            for x in piles:
                curr+=(x+mid-1)//mid
            if curr<=h: #We include the = case because we are already eating fast enough but we want to see how slow we can 
                minim=mid #Remember to keep what the question asks for
                R=mid-1 #Try eating at a slower rate to get a smaller time (not overeating)
            else: #curr>h
                L=mid+1 #Not eating fast enough
        return minim