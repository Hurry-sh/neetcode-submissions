class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        res,rsum=[],0
        temp=0
        for i in nums:
            temp+=i
        def dfs(i,cur,rsum):
            if i==len(nums):
                return
            if rsum==temp/2:
                res.append(cur.copy())
            cur.append(nums[i])
            dfs(i+1,cur,rsum+nums[i])
            cur.pop()
            dfs(i+1,cur,rsum)
        dfs(0,[],rsum)
        print(res)
        if res:
            return True
        else:
            return False