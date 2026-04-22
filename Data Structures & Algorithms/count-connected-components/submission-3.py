class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = { i: [] for i in range(n) }
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        visited = set()
        def dfs(node, prev):
            visited.add(node)

            for neighbour in adj[node]:
                if neighbour not in visited:
                    dfs(neighbour, node)
        
        res = 0
        for i in range(n):
            if i not in visited:
                dfs(i, -1)
                res += 1
        
        return res
