class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        check=defaultdict(int)
        for i in s:
            check[i]+=1
        for j in t:
            check[j]-=1
        for k in check:
            if check[k]!=0:
                return False
        return True
