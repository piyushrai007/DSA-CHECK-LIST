graph = {
  'p' : ['q','s','r'],
  'q' : ['p','r'],
  'r' : ['t','q','p'],
  's' : ['p','t'],
  't' : ['r'],
}

visited = set() 

def dfs(visited, graph, node):   
    if node not in visited:  
        print ("->",node,end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

print("Following is the Depth-First Search")
dfs(visited, graph, 'p')