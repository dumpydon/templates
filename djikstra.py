#---template-------------------------------------------------------------------------------------------------------
    def dijkstra(self, n, adj, S):
        
        pq = [] #{dist, node} will give based on shortst (dist) {keep dist, then node}
        
        # Initialising dist list with 10**18 to indicate the nodes are unvisited initially
        dist = [10**18] *n 
        dist[src] = 0
        
        heapq.heappush(pq, (0, src))

        while pq:
            d, node = heapq.heappop(pq)

            for nei, edgw in adj[node]:

                if d + edgw < dist[nei]:
                    dist[nei] = d + edgw

                    heapq.heappush(pq, (dist[nei], nei))

        return dist
