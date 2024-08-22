class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            adj[course].append(prereq)
            
        visit = {}
        
        def dfs(c):
            if c in visit:
                return visit[c]
            visit[c] = False
            for pre in adj[c]:
                if not dfs(pre):
                    return False
            visit[c] = True
            return True
            
        for c in range(numCourses):
            if not dfs(c):
                return False
            
        return True