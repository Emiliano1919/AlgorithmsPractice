class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lastIdx={}
        L=0
        res=0
        for R in range(len(s)):
            if s[R] in lastIdx:
                L=max(L,lastIdx[s[R]]+1)
            lastIdx[s[R]]=R
            res=max(R-L+1,res)
        return res
            

                
                