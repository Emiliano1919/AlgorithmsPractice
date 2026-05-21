class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones)>1:
            first=heapq.heappop_max(stones)
            second=heapq.heappop_max(stones)
            if first<second:
                newStone=second-first
                heapq.heappush_max(stones,newStone)
            elif second<first: 
                #This part is not really clear on the text.
                newStone=first-second
                heapq.heappush_max(stones,newStone)
        if len(stones)==1:
            return heapq.heappop_max(stones)
        else:
            return 0