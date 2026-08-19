class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        org=defaultdict(list)
        for i,val in enumerate(nums):
            org[val].append(i)
        nums.sort() 
        i=0
        j=len(nums)-1
        while i<j:
            cur=nums[i]+nums[j]
            if cur==target:
                indices = org[nums[i]] + org[nums[j]] if nums[i] != nums[j] else org[nums[i]]
                return [min(indices), max(indices)]
            elif cur<target:
                i+=1
            elif cur>target:
                j-=1
        return []