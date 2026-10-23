class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=defaultdict(int)
        heap=[]
        res=[]
        for x in nums:
            freq[x]+=1
        for x,n in freq.items():
            heapq.heappush(heap,(n,x))
            if len(heap)>k:
                heapq.heappop(heap)
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
            