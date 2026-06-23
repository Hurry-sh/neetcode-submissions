class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashdict={}
        for i in nums:
            if i not in hashdict:
                hashdict[i]=hashdict.get(i,0)+1
            hashdict[i]+=1
        for i,n in hashdict.items():
            if n > len(nums)//2:
                return i
        
        