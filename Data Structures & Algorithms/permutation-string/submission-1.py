class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1w=[0]*26
        for x in s1:
            s1w[ord(x)-ord('a')]+=1
        L=0
        s2w=[0]*26
        for R in range(len(s2)):
            if R-L+1>(len(s1)):
                s2w[ord(s2[L])-ord('a')]-=1
                L+=1
            s2w[ord(s2[R])-ord('a')]+=1
            if s2w==s1w:
                return True
        return False

