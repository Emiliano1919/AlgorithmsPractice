class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L=0
        R=len(nums)-1
        while L<=R:
            m=L+(R-L)//2
            if nums[m]==target:
                return m
            if nums[m]>nums[R]:
                if nums[L]<=target<nums[m]:
                    R=m-1
                else:
                    L=m+1
            else:
                #nums[m]<=nums[R]
                if nums[m]<target<=nums[R]:
                    L=m+1
                else:
                    R=m-1
        return -1
