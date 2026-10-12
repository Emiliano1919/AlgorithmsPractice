class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low=math.inf
        maxInc=0
        for x in prices:
            maxInc=max(maxInc,x-low)
            if x<low:
                low=x
        return maxInc