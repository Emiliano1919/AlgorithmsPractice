class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightMax = -1
        for i in range(len(arr)-1,-1,-1):
            newMax = max(arr[i],rightMax) 
            # Compare with current position in case it is the newMax (before replacement)
            arr[i]=rightMax
            # Now that you have updated with rightMax update the newMax
            rightMax = newMax 
        return arr
        