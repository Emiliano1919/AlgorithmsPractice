class Solution:
    def findMin(self, nums: List[int]) -> int:
        L=0
        R=len(nums)-1
        while L<R:
            mid=L+(R-L)//2
            if nums[mid]>nums[R]:
                #so then the mid is bigger than anything else on the right
                L=mid+1
            else:
                #nums[mid]<=nums[R]
                R=mid
        return nums[L] #We are exiting when L==R