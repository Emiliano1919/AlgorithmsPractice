class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre=[0]*len(nums)
        for i in range(len(nums)):
            if i==0:
                pre[i]=nums[i]*1
            else:
                pre[i]=nums[i]*pre[i-1]
        pst=[0]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            if i==len(nums)-1:
                pst[i]=nums[i]*1
            else:
                pst[i]=nums[i]*pst[i+1]
        res=[0]*len(nums)
        for i in range(len(nums)):
            if i==0:
                res[i]=1*pst[i+1]
            elif i==len(nums)-1:
                res[i]=pre[i-1]
            else:
                res[i]=pre[i-1]*pst[i+1]
        return res