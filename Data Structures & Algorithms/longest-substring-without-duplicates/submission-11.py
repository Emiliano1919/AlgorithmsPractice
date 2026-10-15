class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lastIdx={}
        res=0
        L=0
        for R in range(len(s)):
            if s[R] in lastIdx:
                #REMEMBER ABBA
                L=max(lastIdx[s[R]]+1,L)
            lastIdx[s[R]]=R
            res=max(R-L+1,res)
        return res
