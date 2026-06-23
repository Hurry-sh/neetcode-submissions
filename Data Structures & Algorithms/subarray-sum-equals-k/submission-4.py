class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res=cursum=0
        hashmap={0:1}
        for i in nums:
            cursum+=i
            diff=cursum-k
            res+=hashmap.get(diff,0)
            hashmap[cursum]=1+hashmap.get(cursum,0)
        return res
