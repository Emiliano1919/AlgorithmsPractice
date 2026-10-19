class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        for i,k in enumerate(nums):
            if k>0:
                break
            if i>0 and nums[i]==nums[i-1]:
                continue
            L=i+1 
            R=len(nums)-1
            while L<R:
                val=k+nums[L]+nums[R]
                if val==0:
                    res.append([k,nums[L],nums[R]])
                    
                    L+=1
                    R-=1
                    while L<R and nums[L]==nums[L-1]:
                        L+=1
                elif val<0:
                    L+=1
                else:
                    R-=1
        return res