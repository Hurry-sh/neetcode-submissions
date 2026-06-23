class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        new_nums = []
        for num in nums:
            if num not in seen:
                seen.add(num)
                new_nums.append(num)
        nums[:] = new_nums  # modify original list
        return len(nums)
