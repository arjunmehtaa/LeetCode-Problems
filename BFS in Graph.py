# BFS in Graph (given Adjecency List)             
                
def traverseBFS(graph):
    queue = [0]
    seen = {}
    ans = []
    while len(queue):
        vertex = queue.pop(0)
        seen[vertex] = true
        ans.append(vertex)
        connections = graph[vertex]
        for i in range(0, len(connections)):
            connection = connections[i]
            if not seen[connection]:
                queue.append(connection)
