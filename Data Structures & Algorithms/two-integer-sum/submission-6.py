class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        org =[]
        for i, num in enumerate(nums):
            org.append([num,i])
        org.sort()
        i,j=0,len(nums)-1
        while i<j:
            cur=org[i][0]+org[j][0]
            if cur==target:
                return [min(org[i][1],org[j][1]),max(org[i][1],org[j][1])]
            elif cur<target:
                i+=1
            else:
                j-=1
        return []