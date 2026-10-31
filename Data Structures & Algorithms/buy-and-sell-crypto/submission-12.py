class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice=prices[0]
        maxP=0
        for p in prices:
            maxP=max(maxP,p-minPrice)
            minPrice=min(minPrice,p)
        return maxP