class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count=defaultdict(int)
        maxWindow=0
        L=R=0
        while R<len(s):
            while count[s[R]]>0:
                count[s[L]]-=1
                L+=1
            maxWindow=max(maxWindow,R-L+1)
            count[s[R]]+=1
            R+=1
        return maxWindow
