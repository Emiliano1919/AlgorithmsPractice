class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L=0
        minLow=prices[L]
        maxi=0
        for R in range(1,len(prices)):
            curr=prices[R]
            maxi=max(curr-minLow,maxi)
            while minLow>curr:
                L+=1 #The while loop self corrects the updating of the minLow even if we do L+=1 after the update the while loop will just run again and update correctly
                minLow=prices[L]
        return maxi

            