class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookUp=defaultdict(list)
        for i in range(len(nums)):
            x=nums[i]
            diff=-(x-target)
            if diff in lookUp:
                return [lookUp[diff][0],i]
            lookUp[x].append(i)