class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adjList = {}
        for i in range(0, len(manager)):
            if manager[i] in adjList:
                adjList[manager[i]].append(i)
            else:
                adjList[manager[i]] = [i]
        return traverse(informTime, adjList, headID)

def traverse(informTime, adjList, root):
    max_time = 0
    if root in adjList:
        for i in range(0, len(adjList[root])):
            branch_time = traverse(informTime, adjList, adjList[root][i])
            max_time = max(max_time, branch_time)
    return max_time + informTime[root]