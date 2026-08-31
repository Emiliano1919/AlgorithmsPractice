class Solution:

    def encode(self, strs: List[str]) -> str:
        res=''
        for s in strs:
            res+= str(len(s))+'#'+s
        return res
    def decode(self, s: str) -> List[str]:
        res=[]
        L=R=0
        while R<len(s):
            while s[R]!='#':
                R+=1
            length=int(s[L:R])
            res.append(s[R+1:R+length+1])
            L=R=R+length+1
        return res
