class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L=0
        mpFreq=defaultdict(int)
        maxFreq=0
        maxWindow=0
        for R in range(len(s)):
            mpFreq[s[R]]+=1
            maxFreq=max(maxFreq,mpFreq[s[R]])
            if (R-L+1)-maxFreq>k:
                mpFreq[s[L]]-=1 #So that we don't ruin the count if we find it again
                L+=1
            maxWindow=max((R-L+1),maxWindow)
        return maxWindow
            
