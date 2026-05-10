class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        length= len(nums)
        prefixSum=[0]*(length+1) #We put extra length for the inital 0
        for i in range(length):
            prefixSum[i+1]=prefixSum[i]+nums[i]
        for i in range(length):
            leftSum=prefixSum[i]
            rightSum=prefixSum[length]-prefixSum[i+1] 
            # This takes care of the zero if we index at the end
            # It also takes care of generating postfix without calculating another array
            if leftSum == rightSum:
                return i
        return -1

