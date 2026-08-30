class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ref=[0]*26
        for x in s1:
            ref[ord(x)-ord('a')]+=1
        L=0
        window=[0]*26
        for R in range(len(s2)):
            if R-L+1>len(s1):
                window[ord(s2[L])-ord('a')]-=1
                L+=1
            window[ord(s2[R])-ord('a')]+=1
            print(window)
            if window==ref:
                return True
        return False


            