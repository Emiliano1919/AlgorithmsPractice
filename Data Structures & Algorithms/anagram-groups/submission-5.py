class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookUp=defaultdict(list)
        for s in strs:
            dic=[0]*26
            for x in s:
                dic[ord(x)-ord('a')]+=1
            lookUp[tuple(dic)].append(s)
        return list(lookUp.values())
