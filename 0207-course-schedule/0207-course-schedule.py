class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}
        
        for pre in prerequisites:
            adj[pre[0]].append(pre[1])
        
        def dfs(c, visit):
            if c in visit:
                return False
            if adj[c] == []:
                return True
            visit.add(c)
            for p in adj[c]:
                if not dfs(p, visit):
                    return False
            visit.remove(c)
            adj[c] = []
            return True
            
        for i in range(numCourses):
            visit = set()
            if not dfs(i, visit):
                return False
            
        return True
                