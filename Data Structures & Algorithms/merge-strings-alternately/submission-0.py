class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        str=""
        for i in range (min(len(word1),len(word2))):
            str+=word1[i]
            str+=word2[i]
        if len(word1)<len(word2):
            i=len(word1)
            str+=word2[i:]
        elif len(word1)>len(word2):
            i=len(word2)
            str+=word1[i:]
        return str