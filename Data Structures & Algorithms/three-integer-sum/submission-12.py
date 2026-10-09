class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, n in enumerate(nums):
            if i > 0 and n == nums[i - 1]:
                continue
            L = i + 1
            R = len(nums) - 1
            while L < R:
                if nums[L] + nums[R] == -n:
                    res.append([nums[i], nums[L], nums[R]])
                    L += 1
                    R -= 1
                    while L < R and nums[L] == nums[L - 1]:
                        L += 1
                elif nums[L] + nums[R] < -n:
                    L += 1
                else:
                    R -= 1
        return res
