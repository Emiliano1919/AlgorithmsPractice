# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        BigList=[]
        if len(pairs)==0:
            return BigList
        BigList.append(pairs[:]) 
        # We need to add at the start
        for i in range(1,len(pairs)):
            j=i-1
            while j>=0 and pairs[j+1].key<pairs[j].key:
                tmp=pairs[j+1]
                pairs[j+1]=pairs[j]
                pairs[j]=tmp
                j-=1
            #You have to put it at the end because the last one ends here
            BigList.append(pairs[:]) #Otherwise remember that lists are objects so they are pass by reference
        return BigList
            

