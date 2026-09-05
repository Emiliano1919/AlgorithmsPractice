class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L=0
        R=len(nums)-1
        while L<=R:
            mid=L+(R-L)//2
            if nums[mid]==target:
                return mid
            #Left side ordered
            if nums[L]<=nums[mid]: #Single element resistant
                if nums[L]<=target<nums[mid]:
                    #Target can be L but cannot be mid because of first check
                    R=mid-1
                else:
                    L=mid+1
            else:
                if nums[mid]<target<=nums[R]:
                    #Target can be R but cannot be mid because of first check
                    L=mid+1
                else:
                    R=mid-1
        return -1

                