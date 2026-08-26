class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookUp=defaultdict(list)
        for s in strs:
            l=[0]*26
            for i in s:
                l[ord(i)-ord('a')]+=1
            lookUp[tuple(l)].append(s)
        res=[]
        for k in lookUp:
            res.append(lookUp[k])
        return res
