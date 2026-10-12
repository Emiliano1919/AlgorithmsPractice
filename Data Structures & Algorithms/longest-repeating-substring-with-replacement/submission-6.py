class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxWindow=0
        freq=defaultdict(int)
        maxFreq=0
        L=0
        for R in range(len(s)):
            freq[s[R]]+=1
            maxFreq=max(freq[s[R]],maxFreq)
            
            if (R-L+1)-maxFreq>k:
                freq[s[L]]-=1
                L+=1
            maxWindow=max(R-L+1,maxWindow)
        return maxWindow