from collections import defaultdict

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)

        for a, b in connections:
            graph[a].append((b, 1))
            graph[b].append((a, 0))

        visited = set()
        ans = 0

        def dfs(city):
            nonlocal ans
            visited.add(city)

            for nei, cost in graph[city]:
                if nei not in visited:
                    ans += cost
                    dfs(nei)

        dfs(0)
        return ans