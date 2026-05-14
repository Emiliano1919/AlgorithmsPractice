class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L,R=1,max(piles)
        res =R # The first answer is the maximal
        while L<=R:
            k=L+(R-L)//2
            totalTime=0
            for p in piles:
                totalTime +=math.ceil(float(p)/k)
            if totalTime <= h:
                res=k 
                #Next time if you know there is an edge case cover it just in case
                #Figure out the input later
                R=k-1
            else:
                L=k+1
        return res 