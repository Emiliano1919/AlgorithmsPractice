class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        exist=set()
        res=0
        for x in nums:
            exist.add(x)
        for x in exist:
            cur=1
            res=max(res,cur)
            if x-1 not in exist:
                z=x+1
                while z in exist:
                    z+=1
                    cur+=1
                    res=max(res,cur)
        return res