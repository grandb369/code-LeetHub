class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        cache = {}
        def dfs(node, mask):
            state = (node, mask)
            # Base Case
            if state in cache:
                return cache[state]
            if mask & (mask - 1) == 0:
                return 0
            # Init cache[state] to infinity to avoid endless loop between two nodes
            cache[state] = float('inf')
            for neighbor in graph[node]:
                if mask & (1 << neighbor):
                    # If already visited currentNode mask doesn't change
                    visited = 1 + dfs(neighbor, mask)
                    # If not visited currentNode set mask = mask ^ (1 << node)
                    notVisited = 1 + dfs(neighbor, mask ^ (1 << node))
                    cache[state] = min(cache[state], visited, notVisited)
            return cache[state]
        
        endingMask = (1 << len(graph)) - 1
        cache = {}
        
        return min(dfs(node, endingMask) for node in range(len(graph)))