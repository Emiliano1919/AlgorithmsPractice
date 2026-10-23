class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        for i, k in enumerate(nums):
            if k>0:
                #a+b+c=0 and if a>b>c and c>0 then a+b+c neq 0
                break
            if i>0 and nums[i]==nums[i-1]:
                continue
            L=i+1
            R=len(nums)-1
            while L<R:
                curr=nums[L]+nums[R]+k
                if curr==0:
                    res.append([k,nums[L],nums[R]])
                    L+=1
                    R-=1 #Not sure about this part
                    while L<R and nums[L]==nums[L-1]:
                        L+=1
                elif curr>0: #If we do an if here we will increment after the while loop again (And we want to check if we landed correctly)
                    R-=1
                else:
                    L+=1
        return res


            