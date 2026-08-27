class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for k in range(len(nums)):
            if k > 0 and nums[k] == nums[k-1]:
                continue
            x = nums[k]
            i=k+1
            j=len(nums)-1
            while i<j:
                if nums[i]+nums[j]==-x:
                    res.append([nums[i],nums[j],x])
                    i+=1
                    j-=1
                    while i < j and nums[i] == nums[i-1]:
                        i += 1
                elif nums[i]+nums[j]<-x:
                    i+=1
                else:
                    j-=1
        return res