# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.quickSortHelper(pairs,0,len(pairs)-1)
    def quickSortHelper(self,arr:List[Pair],s: int, e:int):
        if e-s+1<=1:
            return arr
        
        left=s
        for i in range(s,e): #Important to start at s because right side
            if arr[i].key<arr[e].key:
                tmp=arr[i]
                arr[i]=arr[left]
                arr[left]=tmp
                left+=1
        
        tmp=arr[left]
        arr[left]=arr[e]
        arr[e]=tmp
        
        self.quickSortHelper(arr,s,left-1)
        self.quickSortHelper(arr,left+1,e)

        return arr

