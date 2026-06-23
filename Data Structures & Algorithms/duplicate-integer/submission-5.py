class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap={}
        for i in nums:
            if i not in hashmap:
                hashmap[i]=hashmap.get(i,0)
            hashmap[i]+=1
            if hashmap[i]>1:
                return True
        return False