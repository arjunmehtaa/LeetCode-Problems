# BFS in Graph (given Adjecency List)
    
def traverseBFS(graph):
    queue = [0]
    values = []
    seen ={}
    while(len(queue) > 0):
        vertex = queue.pop(0)
        values.push(vertex)
        seen[vertex] = true
        connections = graph[vertex]
        for i in range(0, len(connections)):
            connection = connections[i]
            if not seen[connection]:
                queue.append(i)
