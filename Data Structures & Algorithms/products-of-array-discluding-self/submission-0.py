class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        prefix=[1]*n
        postfix=[1]*n
        ans=[1]*n
        for i in range(n):
            prefix[i]=nums[i]*prefix[i-1] if i>0 else nums[i]
            # Note:Remember that going to the right is more not less
            postfix[n-1-i]=nums[n-1-i]*postfix[n-i] if i>0 else nums[n-1-i]
        for i in range(n):
            if i==0:
                ans[i]=postfix[i+1]
            elif i==n-1:
                ans[i]=prefix[i-1]
            else:
                ans[i]=prefix[i-1]*postfix[i+1]
        return ans