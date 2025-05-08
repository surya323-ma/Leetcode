from typing import List
import heapq

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        INF = 10**30
        dist = [[[INF]*2 for _ in range(m)] for _ in range(n)]
        dist[0][0][0] = 0 
        pq = [(0, 0, 0, 0)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while pq:
            t, x, y, p = heapq.heappop(pq)
            if x == n-1 and y == m-1:
                return t
            
            # skip stale entries
            if t > dist[x][y][p]:
                continue
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    step_cost = 1 if p == 0 else 2
                    depart = max(t, moveTime[nx][ny])
                    arrival = depart + step_cost
                    np = p^1 
                    if arrival < dist[nx][ny][np]:
                        dist[nx][ny][np] = arrival
                        heapq.heappush(pq, (arrival, nx, ny, np))
        
        # in case only one parity reaches the goal
        return min(dist[n-1][m-1])
