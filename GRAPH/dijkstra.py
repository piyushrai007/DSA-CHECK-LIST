import heapq
class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        #code here
        min_heap = []
        
        dist = [10000000000]*V
        dist[S]=0
        heapq.heappush(min_heap,(0,S))

        while min_heap:
            a= heapq.heappop(min_heap)
            dis = a[0]
            node = a[1]
            for adjnode, weight in adj[node]:  # Unpack directly
                if dis + weight < dist[adjnode]:
                    dist[adjnode] = dis + weight
                    heapq.heappush(min_heap, (dist[adjnode], adjnode))
            
        return dist