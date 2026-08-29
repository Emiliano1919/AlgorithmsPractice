class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L=0
        longest=0
        repeat=set()
        for R in range(len(s)):
            while s[R] in repeat:
                repeat.remove(s[L])
                L+=1
            repeat.add(s[R])
            longest=max(R-L+1,longest)
        return longest



