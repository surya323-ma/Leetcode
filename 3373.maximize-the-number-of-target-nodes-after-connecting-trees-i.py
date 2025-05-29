There exist two undirected trees with n and m nodes, labeled from [0, n - 1] and [0, m - 1], respectively.
You are given two 2D integer arrays edges1 and edges2 of lengths n - 1 and m - 1, respectively, where edges1[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the first tree and edges2[i] = [ui, vi] indicates that there is an edge between nodes ui and vi in the second tree.
Node u is target to node v if the number of edges on the path from u to v is even. Note that a node is always target to itself.
Return an array of n integers answer, where answer[i] is the maximum possible number of nodes that are target to node i of the first tree if you had to connect one node from the first tree to another node in the second tree.

Note that queries are independent from each other. That is, for every query you will remove the added edge before proceeding to the next query.
#code here

from collections import deque

class Solution:
    def maxTargetNodes(self, edges1, edges2):
        def build_adj_list(edges):
            n = len(edges) + 1
            adj = [[] for _ in range(n)]
            for u, v in edges:
                adj[u].append(v)
                adj[v].append(u)
            return adj
        
        def bfs_count(adj):
            color = [-1] * len(adj)
            queue = deque([0])
            color[0] = 0
            even_count = odd_count = 0
            
            while queue:
                u = queue.popleft()
                if color[u] == 0:
                    even_count += 1
                else:
                    odd_count += 1

                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = color[u] ^ 1
                        queue.append(v)

            return even_count, odd_count, color

        adjA, adjB = build_adj_list(edges1), build_adj_list(edges2)
        evenA, oddA, colorA = bfs_count(adjA)
        evenB, oddB, _ = bfs_count(adjB)

        maxiB = max(evenB, oddB)
        return [(evenA if colorA[i] == 0 else oddA) + maxiB for i in range(len(adjA))]
