You are given a string s consisting of the characters 'N', 'S', 'E', and 'W', where s[i] indicates movements in an infinite grid:

'N' : Move north by 1 unit.
'S' : Move south by 1 unit.
'E' : Move east by 1 unit.
'W' : Move west by 1 unit.
Initially, you are at the origin (0, 0). You can change at most k characters to any of the four directions.

Find the maximum Manhattan distance from the origin that can be achieved at any time while performing the movements in order.

The Manhattan Distance between two cells (xi, yi) and (xj, yj) is |xi - xj| + |yi - yj|.
class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        d = {'N': 0, 'S': 0, 'E': 0, 'W': 0}
        ans = 0

        for ch in s:
            d[ch] += 1

            dx = abs(d['E'] - d['W'])
            dy = abs(d['N'] - d['S'])

            distance = dx + dy
            distance_lost = (d['E'] + d['W'] - dx) + (d['N'] + d['S'] - dy)
            recovered = min(k, distance_lost // 2)

            ans = max(ans, distance + 2 * recovered)

        return ans


https://leetcode.com/problems/maximum-manhattan-distance-after-k-changes/solutions/6865072/maximum-manhattan-distance-after-k-changes
