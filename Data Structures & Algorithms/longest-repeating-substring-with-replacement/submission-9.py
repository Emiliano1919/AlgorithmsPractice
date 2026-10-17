class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq=defaultdict(int)
        maxWindowSize=0
        maxFreq=0
        L=0
        for R in range(len(s)):
            freq[s[R]]+=1
            maxFreq=max(freq[s[R]],maxFreq)
            if R-L+1-maxFreq>k:
                freq[s[L]]-=1
                L+=1
            maxWindowSize=max(maxWindowSize,R-L+1)
        return maxWindowSize
            