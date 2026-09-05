class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minim=len(nums)
        res=[]
        L=0
        curr=0
        for R in range(len(nums)):
            curr+=nums[R]
            while curr>=target:
                if minim>=R-L+1:
                    minim=R-L+1
                    res=nums[L:R+1]
                curr-=nums[L]
                L+=1
        return len(res)