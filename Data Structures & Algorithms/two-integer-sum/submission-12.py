class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        location=defaultdict(int)
        for i,x in enumerate(nums):
            diff=target-x
            if diff in location:
                return [location[diff],i]
            location[x]=i
