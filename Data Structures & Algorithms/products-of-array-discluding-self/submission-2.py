class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[]
        p=1
        suffix=[0] * len(nums)
        s=1
        for i in range(len(nums)):
            p=nums[i]*p
            s=nums[len(nums)-1-i]*s
            prefix.append(p)
            suffix[len(nums)-1-i] = s
        res=[]
        for i in range(len(nums)):
            pre = prefix[i-1] if i > 0 else 1
            suf = suffix[i+1] if i < len(nums) - 1 else 1
            res.append(pre * suf)
        return res

