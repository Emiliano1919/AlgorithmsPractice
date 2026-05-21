class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones)>1:
            first=heapq.heappop_max(stones)
            second=heapq.heappop_max(stones)
            newStone=abs(first-second)
            if newStone!=0:
                heapq.heappush_max(stones,newStone)
        if len(stones)==1:
            return heapq.heappop_max(stones)
        else:
            return 0