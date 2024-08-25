class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            adj[course].append(prereq)
            
        visit = set()
        def traverse(c):
            if c in visit:
                return False
            if adj[c] == []:
                return True
            visit.add(c)
            for pre in adj[c]:
                if not traverse(pre):
                    return False
            visit.remove(c)
            adj[c] = []
            return True
        
        for i in range(numCourses):
            if not traverse(i):
                return False
            
        return True