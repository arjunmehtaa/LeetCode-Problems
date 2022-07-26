# DFS in Graph (given Adjecency List)             
                
def traverseDFS(vertex, graph, values, seen):
    values.append(vertex)
    seen[vertex] = True    
    connections = graph[vertex]
    for i in range(0, len(connections)):
        connection = connections[i]
        if not seen[connection]:
            traverseDFS(connection, graph, values, seen)
    
def callDFS(graph):
    values = []
    seen = {}
    traverseDFS(0, graph, values, seen)
