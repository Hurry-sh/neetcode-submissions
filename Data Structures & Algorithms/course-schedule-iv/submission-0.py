class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        req = {i: [] for i in range(numCourses)}
        res = {i: set() for i in range(numCourses)}

        for u, v in prerequisites:   # u is prerequisite of v
            req[v].append(u)

        def dfs(course):
            if res[course]:   # already computed
                return res[course]

            for pre in req[course]:
                res[course].add(pre)       # direct prerequisite
                for p in dfs(pre):         # add prereq of prereq
                    res[course].add(p)
            return res[course]

        for i in range(numCourses):
            dfs(i)

        return [u in res[v] for u, v in queries]
