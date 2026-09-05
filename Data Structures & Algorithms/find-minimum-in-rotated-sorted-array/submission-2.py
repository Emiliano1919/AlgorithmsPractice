class Solution:
    def findMin(self, nums: List[int]) -> int:
        L = 0
        R = len(nums) - 1

        while L < R:
            mid = L + (R - L) // 2

            # This portion is already sorted
            if nums[L] <= nums[R]:
                return nums[L]

            if nums[mid] < nums[L]:
                R = mid
            else:
                L = mid + 1

        return nums[L]