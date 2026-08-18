class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check =sorted(nums)
        for i in range(1,len(nums)):
            if check[i]==check[i-1]:
                return True
        return False