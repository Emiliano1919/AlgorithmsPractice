class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        exists={}
        for i in nums:
            if i in exists and exists[i]:
                return True
            exists[i]=True
        return False