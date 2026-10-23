class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        g=set()
        L=0
        R=0
        res=0
        while R<len(s):
            while s[R] in g:
                if s[L] in g:
                    g.remove(s[L])
                L+=1
            g.add(s[R])
            res=max(res,len(g))
            R+=1
        return res
