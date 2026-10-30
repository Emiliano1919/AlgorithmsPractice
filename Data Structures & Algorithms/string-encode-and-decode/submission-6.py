class Solution:

    def encode(self, strs: List[str]) -> str:
        res=''
        for s in strs:
            res+=str(len(s))+"#"+s
        return res
    def decode(self, s: str) -> List[str]:
        L,R=0,0
        res=[]
        while R<len(s):
            if s[R]=="#":
                length=int(s[L:R])
                L=R+1
                R=R+length+1
                res.append(s[L:R])
                L=R
            R+=1
        return res
            
            
