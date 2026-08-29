class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        nums=set(nums)
        maxi=1
        for x in nums:
            if x-1 not in nums:
                curr=1
                y=x
                while y+1 in nums:
                    y+=1
                    curr+=1
                    maxi=max(curr,maxi)
        return maxi
                    
