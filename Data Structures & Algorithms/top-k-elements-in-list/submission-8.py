class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=[[]for _ in range(len(nums)+1)]
        count=defaultdict(int)
        res=[]
        for x in nums:
            count[x]+=1
        for x,number in count.items():
            freq[number].append(x)
        for number in range(len(freq)-1,0,-1):
            for x in freq[number]:
                res.append(x)
                if len(res)==k:
                    return res
        return res