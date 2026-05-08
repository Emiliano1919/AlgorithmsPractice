class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        eliminated=0
        i = 0
        while i < len(nums) - eliminated:#So that we do not iterate over eliminated
            if nums[i]==val:
                k=i
                while k+1<len(nums):
                    nums[k]=nums[k+1]
                    k+=1
                eliminated+=1
            else:
                i += 1
        return len(nums)-eliminated