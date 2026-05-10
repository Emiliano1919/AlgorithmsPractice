class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[1]*n
        prefix=1 #We use the identity for the inital
        for i in range(n):
            ans[i]=prefix #Prefix does not include itself at current position
            prefix *= nums[i]
        postfix=1  #We also use the identity for the last
        for i in range(n-1,-1,-1):
            ans[i]*=postfix #Same with postfix
            postfix*=nums[i]
        return ans