class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = {i: [] for i in range(n)}
        for u, v, w in edges:
            adj[u].append((v, w))
        
        min_h=[(0,src)]
        shortpath={}

        while min_h:
            w1, n1 = heapq.heappop(min_h)

            if n1 in shortpath:
                continue

            shortpath[n1] = w1

            for n2, w2 in adj[n1]:
                if n2 not in shortpath:
                    heapq.heappush(min_h, (w1 + w2, n2))
            
        for i in range(n):
            if i not in shortpath:
                shortpath[i] = -1

        return shortpath