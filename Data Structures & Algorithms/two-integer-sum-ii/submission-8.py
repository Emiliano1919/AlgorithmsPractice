class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L=0
        R=len(numbers)-1
        while L<R:
            currSum=numbers[L]+numbers[R]
            if target>currSum:
                L+=1
            elif target<currSum:
                R-=1
            else:
                return[L+1,R+1]