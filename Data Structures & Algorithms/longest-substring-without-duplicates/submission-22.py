class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L=0
        lstIdx={}
        res=0
        for R in range(len(s)):
            if s[R] in lstIdx:
                L=max(L,lstIdx[s[R]]+1)
            lstIdx[s[R]]=R
            res=max(R-L+1,res)
        return res


