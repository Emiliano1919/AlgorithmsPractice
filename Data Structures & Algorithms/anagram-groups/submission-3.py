class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for i in range(len(strs)):
            k=''.join(sorted(strs[i]))
            res[k].append(strs[i])
        return list(res.values())