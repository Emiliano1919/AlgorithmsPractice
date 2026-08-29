class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L=0
        longest=0
        repeat=set()
        for R in range(len(s)):
            while s[R] in repeat:
                repeat.remove(s[L])
                L+=1
            longest=max(R-L+1,longest) #This can go before or after adding S[R] because we have already eliminated duplicates so it will definetely be added and counted towards the length
            repeat.add(s[R])
            
        return longest



