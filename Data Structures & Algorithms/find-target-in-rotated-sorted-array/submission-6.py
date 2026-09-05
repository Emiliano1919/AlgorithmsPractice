class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L=0
        R=len(nums)-1
        while L<=R:
            mid=L+(R-L)//2
            if nums[mid]==target:
                return mid
            if nums[mid]<=nums[R]:
                if nums[mid]<target<=nums[R]:
                    L=mid+1
                else:
                    R=mid-1
            else:
                if nums[L]<=target<nums[mid]:
                    R=mid-1
                else:
                    L=mid+1
        return -1
