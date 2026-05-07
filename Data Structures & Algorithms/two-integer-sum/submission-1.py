class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        for i in range(len(nums)):
            diff=target-nums[i]
            lookUp=dic.get(diff,None)
            if lookUp==None:
                dic[nums[i]]=i
            else:
                return [lookUp,i]
                #The i is the biggest because lookUp must already be there (we are in else)