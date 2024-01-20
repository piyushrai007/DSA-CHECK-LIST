def bfs(gdict,vertex):
        visited = [vertex]
        queue = [vertex]
        while queue:
            deVertex = queue.pop(0)
            print(deVertex)
            for adjacentVertex in gdict[deVertex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    queue.append(adjacentVertex)
def sssp(gdict,start,end):
    queue = []
    queue.append([start])
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node == end:
            return path
        for adj in gdict[node]:
            new_path = list(path)
            new_path.append(adj)
            queue.append(new_path)
customGraph =  {"a":["b","c"],"b":["d","g"],

                "c":["d","e"],

                "d":["f"]
                 ,"e":["f"],
                 "g" :["f"]
                    
                    }
g = sssp(customGraph,"a","f")
print(g)