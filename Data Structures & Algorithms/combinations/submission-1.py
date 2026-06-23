class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        res=[]
        def dfs(i,cur):
            if len(cur)==k:
                res.append(cur.copy())
                return
            if i >= n:
                return
            cur.append(i+1)
            dfs(i+1,cur)
            cur.pop()
            dfs(i+1,cur)
        dfs(0,[])
        return res
        