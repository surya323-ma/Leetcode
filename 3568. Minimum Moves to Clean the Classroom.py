You are given an m x n grid classroom where a student volunteer is tasked with cleaning up litter scattered around the room. Each cell in the grid is one of the following:
'S': Starting position of the student
'L': Litter that must be collected (once collected, the cell becomes empty)
'R': Reset area that restores the student's energy to full capacity, regardless of their current energy level (can be used multiple times)
'X': Obstacle the student cannot pass through
'.': Empty space
You are also given an integer energy, representing the student's maximum energy capacity. The student starts with this energy from the starting position 'S'.

Each move to an adjacent cell (up, down, left, or right) costs 1 unit of energy. If the energy reaches 0, the student can only continue if they are on a reset area 'R', which resets the energy to its maximum capacity energy.

Return the minimum number of moves required to collect all litter items, or -1 if it's impossible.
from typing import List
from heapq import heappush, heappop

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        litter, sr, sc = [], 0, 0
        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S': sr, sc = i, j
                elif classroom[i][j] == 'L': litter.append((i, j))
        k = len(litter)
        if k == 0: return 0

        id = [[-1]*n for _ in range(m)]
        for i,(r,c) in enumerate(litter): id[r][c] = i
        total_mask, cells = 1<<k, m*n
        best = [-1]*(total_mask*cells)

        pq = [(0, sr, sc, 0, energy)]  # (moves, r, c, mask, e)
        best[sr*n+sc] = energy
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]

        while pq:
            moves,r,c,mask,e = heappop(pq)
            if mask == total_mask-1: return moves
            if e==0: continue
            for dr,dc in dirs:
                nr,nc = r+dr,c+dc
                if not (0<=nr<m and 0<=nc<n) or classroom[nr][nc]=='X': continue
                ne, nmask = e-1, mask
                if classroom[nr][nc]=='R': ne = energy
                if id[nr][nc]!=-1: nmask |= 1<<id[nr][nc]
                pos, idx = nr*n+nc, nmask*cells+nr*n+nc
                if best[idx]>=ne: continue
                best[idx]=ne
                heappush(pq,(moves+1,nr,nc,nmask,ne))
        return -1
