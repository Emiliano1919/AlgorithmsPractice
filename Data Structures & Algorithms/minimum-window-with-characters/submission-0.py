class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need=len(set(t))
        needFreq=defaultdict(int)
        haveFreq={}
        for x in t:
            needFreq[x]+=1
            haveFreq[x]=0
        L=0
        have=0
        minLength=math.inf
        minString=''
        for R in range(len(s)):
            if s[R] in needFreq:
                if (haveFreq[s[R]])+1==needFreq[s[R]]:
                    have+=1
                haveFreq[s[R]]+=1
            
            while have==need:
                if R-L+1 < minLength:
                    minLength=R-L+1
                    minString=s[L:R+1]
                
                if s[L] in needFreq:
                    if haveFreq[s[L]] == needFreq[s[L]]:
                        have-=1
                    haveFreq[s[L]]-=1
                L+=1
        return minString
            

