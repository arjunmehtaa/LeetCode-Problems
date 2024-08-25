# Time Complexity   : O(P + N) (P = WHERE SIZE OF PREREQ LIST)
# Space Complexity  : O(P + N)

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # map each course to prereq list (create adj list)
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
            
        # visitSet - all courses along current dfs path
        visitSet = set()
        def dfs(crs):
            if crs in visitSet:
                return False
            if preMap[crs] == []:
                return True
            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visitSet.remove(crs)
            preMap[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
    
# Optimal Solution

# Time Complexity   : O(P + N^2) (P = WHERE SIZE OF PREREQ LIST)
# Space Complexity  : O(N^2)

# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
#         in_degree = [0]*numCourses
#         adj_list = {}
#         for i in range(0, len(prerequisites)):
#             in_degree[prerequisites[i][0]] += 1
#             if prerequisites[i][1] in adj_list:
#                 adj_list[prerequisites[i][1]].append(prerequisites[i][0])
#             else:
#                 adj_list[prerequisites[i][1]] = [prerequisites[i][0]]
                
#         for j in range(0, numCourses):
#             if j not in adj_list:
#                 adj_list[j] = []
                
#         stack = []
#         for k in range(0, len(in_degree)):
#             if in_degree[k] == 0:
#                 stack.append(k)
                
#         count = 0
#         while len(stack) > 0:
#             current = stack.pop()
#             count += 1
#             adj = adj_list[current]
#             for n in range(0, len(adj)):
#                 next = adj[n]
#                 in_degree[next] -= 1
#                 if in_degree[next] == 0:
#                     stack.append(next)
                        
#         return count == numCourses
        
# Brute Force Solution

# Time Complexity   : O(P + N^3) (P = WHERE SIZE OF PREREQ LIST)
# Space Complexity  : O(N^2)

# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         adj_list = {}
#         for i in range(0, len(prerequisites)):
#             if prerequisites[i][1] in adj_list:
#                 adj_list[prerequisites[i][1]].append(prerequisites[i][0])
#             else:
#                 adj_list[prerequisites[i][1]] = [prerequisites[i][0]]
                
#         for i in range(0, numCourses):
#             if i not in adj_list:
#                 adj_list[i] = []
        
#         for i in range(0, numCourses):
#             queue = []
#             seen = {}
#             for j in range(0, len(adj_list[i])):
#                 queue.append(adj_list[i][j])
#             while len(queue) > 0:
#                 current = queue.pop(0)
#                 seen[current] = True
#                 if current == i:
#                     return False
#                 adj = adj_list[current]
#                 for k in range(0, len(adj)):
#                     next = adj[k]
#                     if next not in seen:
#                         queue.append(next)
#         return True
                