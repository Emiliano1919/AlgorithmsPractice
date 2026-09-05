class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minim=math.inf
        L=0
        curr=0
        for R in range(len(nums)):
            curr+=nums[R]
            while curr>=target: #Think about should you use a while or an if and why
                if minim>=R-L+1:
                    minim=R-L+1
                curr-=nums[L]
                L+=1
        return 0 if minim==math.inf else minim