def topology(dict):
    stack = []
    visited = []
    for k in list(dict):
        if k not in visited:
            tpu(dict,k,visited,stck)
    return stack
    
def tpu(dict,l,visited,stack):
    visited.append(l)
    for i in dict[v]:
        if i not in visited:
            tpu(dict,i,visited,stack)
    stack.insert(0,v)
def one(dict):
    stack = []
    visited = []
    for k in list(dict):
        if k not in visited:
            visited.append(k)
            for i in dict[k]:
                if i not in visited:
                    visited.append(i)
            stack.insert(0,i)
        stack.insert(0,k)
        
                
        






def func(self,node,graph,visited):
        visited[node]=0
        ans=1
        for i in graph[node]:
            if visited[i]==-1:
                ans&=self.func(i,graph,visited)
            else:
                ans&=visited[i]
        if ans==1:
            visited[node]=1
            return 1
        return 0