class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count=defaultdict(int)
        res=0
        L=0
        maxFreq=0
        for R in range(len(s)):
            count[s[R]]+=1 #Increase count
            maxFreq=max(maxFreq,count[s[R]]) #Update the max frequency

            while (R-L+1)-maxFreq>k: #If window size - the max freq is bigger than k then we have to move the left
                count[s[L]]-=1
                L+=1
            res=max(res,R-L+1)
        return res
        
        