class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adjList = {}
        for i in range(0, len(manager)):
            if manager[i] not in adjList:
                adjList[manager[i]] = [i]
            else:
                adjList[manager[i]].append(i)
        return dfs(adjList, headID, informTime)
        
def dfs(adjList, current, informTime):
    max_time = 0
    if current in adjList:
        subs = adjList[current]
        for i in range(0, len(subs)):
            branch_time = dfs(adjList, subs[i], informTime)
            max_time = max(branch_time, max_time)
    return informTime[current] + max_time