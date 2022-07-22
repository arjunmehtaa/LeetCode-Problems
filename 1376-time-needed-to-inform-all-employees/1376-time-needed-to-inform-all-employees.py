# Time Complexity   : O(N)
# Space Complexity  : O(N)

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adjList = {}
        for i in range(0, len(manager)):
            if manager[i] in adjList:
                adjList[manager[i]].append(i)
            else:
                adjList[manager[i]] = [i]
        return dfs(informTime, adjList, headID)

def dfs(informTime, adjList, current):
    max_time = 0
    if current in adjList:
        subs = adjList[current]
        for i in range(0, len(subs)):
            branch_time = dfs(informTime, adjList, subs[i])
            max_time = max(max_time, branch_time)
    return max_time + informTime[current]