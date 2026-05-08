class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_val,count=0,0
        j=0
        while j<len(nums):
            if nums[j]==1:
                count += 1
            else:
                count=0
            if count>max_val: #Remember to update even if you dont have a 0
                max_val=count
            j+=1
        return max_val