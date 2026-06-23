class Solution:
    def rob(self, nums: List[int]) -> int:

        return max(nums[0],
        self.helper(nums[1:]),
        self.helper(nums[:-1]))

    def helper(self,nums):
        
        one,two=0,0
        for num in nums:
            temp=max(one+num,two)
            one=two
            two=temp
        return two
    