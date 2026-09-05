class Solution:
    def findMin(self, nums: List[int]) -> int:
        L=0
        R=len(nums)-1
        while L<R:
            mid=L+(R-L)//2
            if nums[mid]>nums[R]:
                L=mid+1
            else: #nums[mid]<nums[L] and normal case and == (does not need to be taken into account because == does not happen unless we end loop because elements are unique)
                R=mid
                
        return nums[L]