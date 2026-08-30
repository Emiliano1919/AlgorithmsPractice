class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L=0
        maxFreq=0
        window=0
        freq=defaultdict(int)
        for R in range(len(s)):
            freq[s[R]]+=1
            maxFreq=max(maxFreq,freq[s[R]])
            if (R-L+1)-maxFreq>k:
                freq[s[L]]-=1
                L+=1
            window=max(window,R-L+1)
        return  window
            