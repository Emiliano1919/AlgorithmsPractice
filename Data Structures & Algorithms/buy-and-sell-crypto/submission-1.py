class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L=0
        minLow=prices[L]
        maxi=0
        for R in range(1,len(prices)):
            curr=prices[R]
            maxi=max(curr-minLow,maxi)
            while minLow>curr:
                L+=1
                minLow=prices[L]
        return maxi

            