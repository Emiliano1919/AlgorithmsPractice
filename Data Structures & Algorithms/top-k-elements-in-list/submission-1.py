class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for i in nums:
            freq[i]=1+ freq.get(i,0)
        heap=[]
        for num, cnt in freq.items():
            heap.append([cnt, num])
        heapq._heapify_max(heap)

        res = []
        while len(res) < k:
            res.append(heapq._heappop_max(heap)[1])
        return res