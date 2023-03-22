from typing import List, Tuple
from collections import deque
import math

class Solution:
    def bfs(self, n: int, adj: List[List[Tuple[int, int]]]) -> int:
        visited = [False] * (n+1)
        q = deque()
        min_score = math.inf

        q.append(1)
        visited[1] = True

        while q:
            node = q.popleft()

            for neighbor, weight in adj[node]:
                min_score = min(min_score, weight)
                if not visited[neighbor]:
                    visited[neighbor] = True
                    q.append(neighbor)

        return min_score

    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = [[] for _ in range(n+1)]

        for road in roads:
            adj[road[0]].append((road[1], road[2]))
            adj[road[1]].append((road[0], road[2]))

        return self.bfs(n, adj)
