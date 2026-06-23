class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res += str(len(i)) + "#" + i
        print(res)
        return res


    def decode(self, s: str) -> List[str]:
        res = list()
        i = 0

        # Okay so the delimiter is used cause what if the number of words is 10, 69 etc? Your first method of not using "#" will not work!

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length

        return res
    
            
            





