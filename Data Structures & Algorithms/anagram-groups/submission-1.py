class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for s in strs:
            hash=[0]*26
            for c in s:
                hash[ord(c)-ord('a')]+=1
            res[tuple(hash)].append(s)
        return list(res.values())