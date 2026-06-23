class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash={}
        for i in nums:
            if i not in hash:
                hash[i]=1+hash.get(i,0)
            hash[i]+=1
        n=len(nums)/2
        for i,val in hash.items():
            if val>n:
                return i