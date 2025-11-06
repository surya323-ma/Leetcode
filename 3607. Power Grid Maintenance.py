You are given an integer c representing c power stations, each with a unique identifier id from 1 to c (1‑based indexing).

These stations are interconnected via n bidirectional cables, represented by a 2D array connections, where each element connections[i] = [ui, vi] indicates a connection between station ui and station vi. Stations that are directly or indirectly connected form a power grid.

Initially, all stations are online (operational).

You are also given a 2D array queries, where each query is one of the following two types:

[1, x]: A maintenance check is requested for station x. If station x is online, it resolves the check by itself. If station x is offline, the check is resolved by the operational station with the smallest id in the same power grid as x. If no operational station exists in that grid, return -1.
[2, x]: Station x goes offline (i.e., it becomes non-operational).
Return an array of integers representing the results of each query of type [1, x] in the order they appear.
Note: The power grid preserves its structure; an offline (non‑operational) node remains part of its grid and taking it offline does not alter connectivity.
class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        self.parent[self.find(y)] = self.find(x)

class Solution:
    def processQueries(self, c, connections, queries):
        from collections import defaultdict
        import bisect

        dsu = DSU(c)
        for u, v in connections:
            dsu.union(u, v)

        groups = defaultdict(list)
        for i in range(1, c + 1):
            root = dsu.find(i)
            groups[root].append(i)
        for g in groups.values():
            g.sort()

        offline = [False] * (c + 1)
        res = []

        for typ, x in queries:
            root = dsu.find(x)
            arr = groups[root]
            if typ == 1:
                if not offline[x]:
                    res.append(x)
                else:
                    res.append(arr[0] if arr else -1)
            else:
                if not offline[x]:
                    offline[x] = True
                    idx = bisect.bisect_left(arr, x)
                    if idx < len(arr) and arr[idx] == x:
                        arr.pop(idx)
        return res
