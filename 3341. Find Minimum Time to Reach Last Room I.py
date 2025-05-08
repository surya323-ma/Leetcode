There is a dungeon with n x m rooms arranged as a grid.
You are given a 2D array moveTime of size n x m, where moveTime[i][j] represents the minimum time in seconds when you can start moving to that room. You start from the room (0, 0) at time t = 0 and can move to an adjacent room. Moving between adjacent rooms takes exactly one second.
Return the minimum time to reach the room (n - 1, m - 1).
Two rooms are adjacent if they share a common wall, either horizontally or vertically.
#code here
  class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m, n = len(moveTime), len(moveTime[0])
        min_time = [[inf]*n for _ in range(m)]
        min_time[0][0] = 0
        heap = [(0, 0, 0)] 
        while heap:
            t, i, j = heappop(heap)
            if i == m-1 and j == n-1:
                return t
            if t == min_time[i][j]:
                for ii, jj in (i-1, j), (i+1, j), (i, j-1), (i, j+1):
                    if 0 <= ii < m and 0 <= jj < n:
                        tt = max(t, moveTime[ii][jj]) + 1
                        if min_time[ii][jj] > tt:
                            min_time[ii][jj] = tt
                            heappush(heap, (tt, ii, jj))
     
