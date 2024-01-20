class disjoint():
    def __init__(self,n):
        self.parent = [0]*(n+1)
        self.rank = [0]*(n+1)
        for i in range(n):
            self.parent[i]=i
    def findparent(self,node):
        if node==self.parent[node]:
            return node
        self.parent[node]=self.findparent(self.parent[node])
        return self.parent[node] 
    def unionbyrank(self,u,v):
        ult_u = self.findparent(u)
        ult_v = self.findparent(v)
        if ult_u == ult_v:return 
        if self.rank[ult_u]<self.rank[ult_v]:
            self.parent[ult_u]=ult_v
        elif self.rank[ult_v]<self.rank[ult_u]:
            self.parent[ult_v]=ult_u
        else:
            self.parent[ult_u] = self.parent[ult_v]
            self.rank[ult_u]+=1   
a = disjoint(7)
a.unionbyrank(1,2)
a.unionbyrank(6,7)
print(a.findparent(2)==a.findparent(7))
a.unionbyrank(6,2)

print(a.findparent(2)==a.findparent(7))
#User function Template for pytho

class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        #code here
        # print(adj)
        edges = []
        for i in range(V):
            for edjnode,wt in adj[i]:
                edges.append([wt,i,edjnode])
                
        
        d = disjoint(V)
        mst = 0
        edges=sorted(edges)
        for wt,u,v in edges:
            if d.findparent(u)!=d.findparent(v):
                mst+=wt
                d.unionbyrank(u,v)
        return mst