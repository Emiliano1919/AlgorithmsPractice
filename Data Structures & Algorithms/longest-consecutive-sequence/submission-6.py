class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        lookUp=set(nums)
        maxi=1
        for x in lookUp:
            if x-1 not in lookUp:
                cnt=1
                while x+1 in lookUp:
                    x+=1
                    cnt+=1
                maxi=max(cnt,maxi)
        return maxi