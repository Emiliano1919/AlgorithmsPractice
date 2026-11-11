class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice=prices[0]
        maxProfit=0
        for p in prices:
            if minPrice>p:
                minPrice=p
            maxProfit=max(p-minPrice,maxProfit)
        return maxProfit


