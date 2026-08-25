class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        for i in range(len(nums)):
            look=target-nums[i]
            if look in dic:
                return([dic[look], i])
            dic[nums[i]] = i