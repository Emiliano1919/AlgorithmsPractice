class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=defaultdict(int)
        freq=[[]for i in range(len(nums)+1)]

        for x in nums:
            count[x]+=1
        for x,f in count.items():
            freq[f].append(x)

        res=[]
        for i in range(len(freq)-1,0,-1):
            for x in freq[i]:
                res.append(x)
                if len(res)==k:
                    return res