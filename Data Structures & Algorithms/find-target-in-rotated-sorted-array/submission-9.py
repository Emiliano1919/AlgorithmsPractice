class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L=0
        R=len(nums)-1
        while L<=R:
            mid=L+(R-L)//2
            if nums[mid]==target:
                return mid
            if nums[mid]>nums[R]:
                #Right not trie
                if nums[L]<=target<nums[mid]:
                    #Cherche si dans la partie trie
                    R=mid-1
                else:
                    #Sinon discard la partie qui est trie
                    L=mid+1
            else:
                #Trie
                #nums[mid]<=nums[R]
                if nums[mid]<target<=nums[R]:
                    L=mid+1
                else:
                    R=mid-1
        return -1
