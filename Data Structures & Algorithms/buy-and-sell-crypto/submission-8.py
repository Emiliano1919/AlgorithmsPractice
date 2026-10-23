class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxim=0
        L,R=0,1
        while R<len(prices):
            if prices[R]>prices[L]:
                curr=prices[R]-prices[L]
                maxim=max(curr,maxim)
            else:
                L=R
            R+=1
        return maxim

