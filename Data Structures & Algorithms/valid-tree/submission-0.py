class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = { i: [] for i in range(n) }
        for node, neighbour in edges:
            adj[node].append(neighbour)
            adj[neighbour].append(node)

        visited = set()
        def dfs(node, prev):
            if node in visited: return False

            visited.add(node)
            for neighbour in adj[node]:
                if neighbour == prev:
                    continue
                if not dfs(neighbour, node):
                    return False
            return True

        if not dfs(0, -1): return False
        if len(visited) != n: return False
        return True    
            