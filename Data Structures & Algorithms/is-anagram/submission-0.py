class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic={}
        for i in s:
            dic[i] = dic.get(i, 0) + 1
        for k in t:
            if dic.get(k, 0) == 0:
                return False
            dic[k] -= 1 
            #This reduces the count in case we have multiple of the same
        return True
