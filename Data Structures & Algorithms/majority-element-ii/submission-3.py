class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashdict = {}
        res = []

        for i in nums:
            hashdict[i] = hashdict.get(i, 0) + 1   # increment count safely

        for num, count in hashdict.items():
            if count > len(nums) // 3:             # should be ">" not ">="
                res.append(num)

        return res