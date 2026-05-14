class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        buckets=[0]*3
        for n in nums:
            buckets[n]+=1
        
        i=0
        # Suppose we don't have it easy it is not 0,1,2 but something else. How do we do it?
        for j in range(len(buckets)): #I think I could change this to fix that
            for _ in range(buckets[j]):
                nums[i]=j
                i+=1