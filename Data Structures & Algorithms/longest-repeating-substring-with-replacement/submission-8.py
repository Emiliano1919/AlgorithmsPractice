class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq=defaultdict(int)
        maxFreq=0
        L=0
        maxWindow=0
        for R in range(len(s)):
            freq[s[R]]+=1
            maxFreq=max(maxFreq,freq[s[R]])
            if (R-L+1)-maxFreq>k:
                freq[s[L]]-=1
                L+=1
            maxWindow=max(maxWindow,(R-L+1))
        return maxWindow