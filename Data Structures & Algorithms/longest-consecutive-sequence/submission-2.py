class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lookUp=set(nums)
        maxi=0
        for x in lookUp:
            if x-1 not in lookUp:
                cnt=0
                y=x
                while y in lookUp:
                    y+=1
                    cnt+=1
                    maxi=max(cnt,maxi)
        return maxi
            
        