class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adjList = {}
        for i in range(0, len(manager)):
            if manager[i] not in adjList:
                adjList[manager[i]] = [i]
            else:
                adjList[manager[i]].append(i)
        return dfs(informTime, headID, adjList)
    
def dfs(informTime, current, adjList):
    max_time = 0
    if current in adjList:
        subs = adjList[current]
        for i in range(0, len(subs)):
            branch_time = dfs(informTime, subs[i], adjList)
            max_time = max(max_time, branch_time)
    return max_time + informTime[current]
            
        