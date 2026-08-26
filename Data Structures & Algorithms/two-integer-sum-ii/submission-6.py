class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        j=len(numbers)-1
        while i<j:
            diff=numbers[i]+numbers[j]-target
            if diff==0:
                return [i+1,j+1]
            if diff>0:
                j-=1
            if diff<0:
                i+=1
        
