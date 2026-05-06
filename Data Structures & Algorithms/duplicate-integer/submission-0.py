class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        there = {}
        for i in nums:
            if i in there:
                return True
            else:
                there[i]=True
        return False