class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lastTime={}
        res=0
        L=0
        for R in range(len(s)):
            if s[R] in lastTime:
                L=max(L,lastTime[s[R]]+1)
            lastTime[s[R]]=R
            res=max(R-L+1,res)
        return res
