class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globMax,globMin=nums[0],nums[0]
        curmax,curmin=0,0
        total=0
        for num in nums:
            curmax=max(curmax+num,num)
            curmin=min(curmin+num,num)
            total+=num
            globMax=max(globMax,curmax)
            globMin=min(globMin,curmin)
        return max(globMax,total-globMin) if globMax>0 else globMax