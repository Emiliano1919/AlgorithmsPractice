class Solution:
    def minWindow(self, s: str, t: str) -> str:
        have=0
        need=len(set(t))
        needFreq=defaultdict(int)
        for x in t:
            needFreq[x]+=1
        haveFreq=defaultdict(int)
        L=0
        minWindow=''
        minSize=math.inf
        for R in range(len(s)):
            if s[R] in needFreq: #Add first
                if haveFreq[s[R]]+1==needFreq[s[R]]:
                    have+=1
                haveFreq[s[R]]+=1
            while have==need: #Record valid, reduce and record valid until no longer valid
                if minSize>=R-L+1:
                    minSize=min(minSize,R-L+1)
                    minWindow=s[L:R+1]
                if s[L] in needFreq:
                    if haveFreq[s[L]]==needFreq[s[L]]:
                        have-=1
                    haveFreq[s[L]]-=1
                L+=1
        return minWindow

            
