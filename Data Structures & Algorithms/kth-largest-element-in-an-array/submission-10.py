import random


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        s = 0
        e = n - 1
        while s <= e:
            if s == e:
                return nums[s]
            pivot_idx = random.randint(s, e)
            nums[pivot_idx], nums[e] = nums[e], nums[pivot_idx]
            pivot = nums[e]
            left=s
            for i in range(s, e):
                if nums[i] < pivot:
                    nums[left], nums[i] = nums[i], nums[left]
                    left += 1
            nums[left], nums[e] = nums[e], nums[left]
            if n - k < left:
                e = left - 1
            elif n - k > left:
                s = left + 1
            else:
                return nums[left]
