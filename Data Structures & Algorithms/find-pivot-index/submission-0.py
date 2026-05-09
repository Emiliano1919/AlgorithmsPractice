class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pf=[]
        sf=[]
        tp,ts=0,0
        for i in range(len(nums)):
            tp+=nums[i]
            pf.append(tp)
            ts+=nums[len(nums)-i-1]
            sf.append(ts)
        sf.reverse()
        for j in range(len(nums)):
            ## The conditions can be simplified, use terniary operations maybe
            if j==0:
                if (len(nums)>1 and sf[j+1]==0) or (len(nums)==1):
                    return j
            elif j==len(nums)-1:
                if pf[j-1]==0:
                    return j
            elif pf[j-1]==sf[j+1]:
                return j
        return -1
