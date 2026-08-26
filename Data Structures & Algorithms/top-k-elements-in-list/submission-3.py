class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for x in nums:
            freq[x]=1+freq.get(x,0)
        heap=[]
        for x,n in freq.items():
            heap.append([n,x])
        heapq.heapify_max(heap)
        res=[]
        for _ in range(k):
            res.append(heapq.heappop_max(heap)[1])
        return res