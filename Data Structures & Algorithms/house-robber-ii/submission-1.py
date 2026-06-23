class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        
        rob1_1,rob2_1=0,0
        for i in range(0,len(nums)-1):
            temp=max(rob1_1+nums[i],rob2_1)
            rob1_1=rob2_1
            rob2_1=temp
        
        rob1_2,rob2_2=0,0
        for i in range(1,len(nums)):
            temp=max(rob1_2+nums[i],rob2_2)
            rob1_2=rob2_2
            rob2_2=temp

        return max(rob2_1,rob2_2)
    