from typing import List
from collections import deque

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        indegrees = [0] * n
        graph = [[] for _ in range(n)]
        for edge in edges:
            graph[edge[0]].append(edge[1])
            indegrees[edge[1]] += 1
        zero_indegree = deque()
        for i in range(n):
            if indegrees[i] == 0:
                zero_indegree.append(i)
        counts = [[0]*26 for _ in range(n)]
        for i in range(n):
            counts[i][ord(colors[i]) - ord('a')] += 1
        max_count = 0
        visited = 0
        while zero_indegree:
            u = zero_indegree.popleft()
            visited += 1
            for v in graph[u]:
                for i in range(26):
                    counts[v][i] = max(counts[v][i], counts[u][i] + (ord(colors[v]) - ord('a') == i))
                indegrees[v] -= 1
                if indegrees[v] == 0:
                    zero_indegree.append(v)
            max_count = max(max_count, max(counts[u]))
        return max_count if visited == n else -1