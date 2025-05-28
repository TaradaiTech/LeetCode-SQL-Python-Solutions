from typing import List
import heapq

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        INF = float('inf')
        dist = [[INF]*m for _ in range(n)]
        dist[0][0] = 0
        
        pq = [(0, 0, 0)]  # (time, i, j)
        while pq:
            t, i, j = heapq.heappop(pq)
            if t > dist[i][j]:
                continue
            if i == n-1 and j == m-1:
                return t
            for di, dj in dirs:
                ni, nj = i+di, j+dj
                if 0 <= ni < n and 0 <= nj < m:
                    start = max(t, moveTime[ni][nj])
                    arr = start + 1
                    if arr < dist[ni][nj]:
                        dist[ni][nj] = arr
                        heapq.heappush(pq, (arr, ni, nj))
        
        return dist[n-1][m-1]