class Solution:
    def countElements(self, arr: List[int]) -> int:
        count=0
        dic=set(arr)
        for i in arr:
            if i+1 in dic:
                count+=1
        return count
        