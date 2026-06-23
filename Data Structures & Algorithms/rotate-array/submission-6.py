class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        i=0
        res=[0]*len(nums)
        for i,ele in enumerate(nums):
            new_index=(i+k)%len(nums)
            res[new_index]+=ele
        nums[:]=res
        return nums
        