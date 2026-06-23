class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap={}
        for i,ele in enumerate(nums):
            if ele in hashmap and i-hashmap[ele]<=k:
                return True
            hashmap[ele]=i
        return False