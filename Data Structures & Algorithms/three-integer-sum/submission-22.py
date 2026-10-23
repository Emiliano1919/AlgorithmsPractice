class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        for i, k in enumerate(nums):
            if k>0:
                #a+b+c==0 so if a>b>c and c>0 then false
                break
            if i>0 and nums[i]==nums[i-1]:
                #We are skipping the first number if it is the same because the pairs would generate a duplicate
                #-1,-1,0,1 example
                continue
            L=i+1
            R=len(nums)-1
            while L<R:
                curr=nums[L]+nums[R]+k
                if curr==0:
                    res.append([nums[L],nums[R],k])
                    L+=1
                    R-=1
                    while L<R and nums[L]==nums[L-1]:
                        L+=1
                elif curr>0:
                    R-=1
                else:
                    L+=1
        return res
            