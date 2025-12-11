You are given a positive integer n, representing an n x n city. You are also given a 2D grid buildings, where buildings[i] = [x, y] denotes a unique building located at coordinates [x, y].
A building is covered if there is at least one building in all four directions: left, right, above, and below.

Return the number of covered buildings.
class Solution:
    def countCoveredBuildings(self, n, buildings):
        from collections import defaultdict
        import bisect

        rows = defaultdict(list)
        cols = defaultdict(list)

        for x, y in buildings:
            rows[x].append(y)
            cols[y].append(x)

        for r in rows: rows[r].sort()
        for c in cols: cols[c].sort()

        ans = 0
        for x, y in buildings:
            row = rows[x]
            col = cols[y]

            i = bisect.bisect_left(row, y)
            j = bisect.bisect_left(col, x)

            if i > 0 and i < len(row)-1 and j > 0 and j < len(col)-1:
                ans += 1

        return ans
