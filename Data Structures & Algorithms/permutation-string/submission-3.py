class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1w = [0] * 26
        s2w = [0] * 26
        for i in range(len(s1)):
            s1w[ord(s1[i])-ord('a')]+=1
            s2w[ord(s2[i])-ord('a')]+=1
        if s1w==s2w:
            return True
        for i in range(len(s1),len(s2)):
            s2w[ord(s2[i])-ord('a')]+=1
            s2w[ord(s2[i-len(s1)])-ord('a')]-=1
            if s1w==s2w:
                return True
        return False
        