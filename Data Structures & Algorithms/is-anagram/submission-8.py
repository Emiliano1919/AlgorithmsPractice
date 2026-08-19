class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        letters=defaultdict(int)
        for i in range(len(s)):
            letters[s[i]]+=1
            letters[t[i]]-=1
        for l in letters:
            if letters[l]!=0:
                return False
        return True

