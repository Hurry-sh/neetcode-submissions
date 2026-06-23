class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        lst = list()

        for index, num in enumerate(nums):
            l = index + 1
            r = len(nums) - 1

            if num > 0:
                break

            if index > 0 and num == nums[index - 1]:
                continue

            while l < r:
                if num + nums[l] + nums[r] == 0:
                    lst.append([num , nums[l] , nums[r]])
                    l+=1
                    r-=1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif num + nums[l] + nums[r] < 0:
                    l+=1
                elif num + nums[l] + nums[r] > 0:
                    r-=1

        return lst

            




