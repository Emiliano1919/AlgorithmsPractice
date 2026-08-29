class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L=0
        minPrice=prices[L]
        maxProfit=0
        for R in range(1,len(prices)):
            profit=prices[R]-minPrice
            maxProfit=max(maxProfit,profit)
            while prices[R]<minPrice:
                L+=1
                minPrice=min(prices[L],minPrice)
        return maxProfit