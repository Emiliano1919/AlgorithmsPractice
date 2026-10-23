class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        big=0
        L=0
        for R in range(len(prices)):
            if prices[R]>prices[L]:
                big=max(prices[R]-prices[L],big)
            else:
                L=R
        return big

