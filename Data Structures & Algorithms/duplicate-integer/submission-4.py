class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        there=set()
        for x in nums:
            if x in there:
                return True
            there.add(x)
        return False