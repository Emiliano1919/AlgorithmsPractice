class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff={}
        for i in range(len(nums)):
            found=diff.get(target-nums[i],None)
            if found is not None:
                if i!=found:
                    return [found,i]
            diff[nums[i]]=i
        return []