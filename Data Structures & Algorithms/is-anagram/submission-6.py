class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash1,hash2={},{}
        for i in s:
            if i not in hash1:
                hash1[i]=hash1.get(i,0)
            hash1[i]+=1
        for j in t:
            if j not in hash2:
                hash2[j]=hash2.get(j,0)
            hash2[j]+=1
        return hash1==hash2