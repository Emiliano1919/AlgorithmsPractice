class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp={}
        L=0
        maxi=0
        for R in range(len(s)):
            if s[R] in mp:
                L=max(mp[s[R]]+1,L)
            mp[s[R]]=R
            maxi=max(R-L+1,maxi)
        return maxi