class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(0 , len(nums)):
        #     for j in range(i+1 , len(nums)):
        #         if nums[i] + nums[j] == target: 
        #             if i < j:
        #                 return i,j
        #             else:
        #                 return j,i

        prevMap = {} # value -> index.

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff] , i]
            prevMap[n] = i
        return 

