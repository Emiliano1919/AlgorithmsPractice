class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        s1w=[0]*26
        for x in s1:
            s1w[ord(x)-ord('a')]+=1
        l=0
        s2w=[0]*26
        for r in range(len(s2)):
            s2w[ord(s2[r])-ord('a')]+=1
            if r-l+1>=len(s1):
                if s1w==s2w:
                    return True
                s2w[ord(s2[l])-ord('a')]-=1
                l+=1
        return False
        