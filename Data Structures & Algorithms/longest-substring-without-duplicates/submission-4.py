class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L=0
        letters=set()
        maxi=0
        for R in range(len(s)):
            while s[R] in letters:
                letters.remove(s[L])
                L+=1
            letters.add(s[R])
            maxi=max(R-L+1,maxi)
        return maxi