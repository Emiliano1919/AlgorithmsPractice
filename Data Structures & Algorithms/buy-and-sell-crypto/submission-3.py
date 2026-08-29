class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L=0
        minLeft=prices[L]
        maxi=0
        for R in range(1,len(prices)):
            maxi=max(prices[R]-minLeft,maxi)
            while minLeft>prices[R]:
                L+=1
                minLeft=prices[L]
        return maxi