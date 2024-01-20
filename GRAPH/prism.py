import heapq
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        #code here
        # print(adj)
        pq = []
        vis = [0]*V
        sum = 0
        heapq.heappush(pq,(0,0,-1))
        mst = []
        while pq:
            it = heapq.heappop(pq)
            node = it[1]
            wt  = it[0]
            if vis[node]==1:continue
            if it[2]!=-1:mst.append([it[2],it[1]])
            vis[node]=1
            sum+=wt
            a= adj
            for adjnode,ewt in adj[node]:
                if vis[adjnode]!=1:
                    heapq.heappush(pq,(ewt,adjnode,node))
        print(mst)
        return sum