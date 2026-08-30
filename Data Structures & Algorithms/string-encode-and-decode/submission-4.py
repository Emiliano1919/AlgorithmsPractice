class Solution:

    def encode(self, strs: List[str]) -> str:
        res=''
        for s in strs:
            res+=str(len(s))+'#'+s
        print(res)
        return res
    def decode(self, s: str) -> List[str]:
        res=[]
        l,r=0,0
        length=0
        while r<len(s):
            if s[r]=='#':
                length=int(s[l:r])
                word=s[r+1:r+1+length]
                res.append(word)
                r+=length
                l=r+1
            r+=1
        return res
            
            
                