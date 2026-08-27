class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for x in range(len(nums)):
            if x > 0 and nums[x]==nums[x-1]: #IF you don't put the 0 check it will compare against the last element because index [-1] is the last
                continue

            i=x+1
            j=len(nums)-1
            while i<j:
                if nums[i]+nums[j]==-nums[x]:
                    res.append([nums[x],nums[i],nums[j]])
                    i+=1
                    j-=1
                    while i<j and nums[j]==nums[j+1]:
                        j-=1
                elif nums[i]+nums[j]<-nums[x]:
                    i+=1
                else:
                    j-=1
        return res
                