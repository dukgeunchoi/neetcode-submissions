class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = { i: [] for i in range(1, len(edges) + 1) }
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        cycle = set()
        def detectCycle(node, prev):
            if node in cycle:
                return True
            cycle.add(node)

            for neighbour in adj[node]:
                if neighbour == prev:
                    continue
                if detectCycle(neighbour, node): return True
            cycle.remove(node)
        
        detectCycle(edges[0][0], -1)
        res = []
        for n1, n2 in edges:
            if n1 in cycle and n2 in cycle:
                res = [n1, n2]
        return res
