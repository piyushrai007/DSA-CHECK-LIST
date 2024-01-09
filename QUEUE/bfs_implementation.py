def bfs(graph,start):
    n = len(graph)
    qe = []
    qe.append(start)
    vis = [0]*n
    vis[start] = 1
    ans = []
    while qe:
        node  = qe[0]
        print(qe.pop(0))
        # qe.pop()

        ans.append(node)
        for k in graph[node]:
            if vis[k] !=1:
                vis[k]=1
                qe.append(k)
    return ans

graph = {0:[],
        1:[2,6],
        2:[3,4],
        3:[2],
        4:[2,5],
        5:[4,8],
        6:[1,7,9],
        7:[8,6],
        8:[7,5],
        9:[6]}
print(bfs(graph,1))      
