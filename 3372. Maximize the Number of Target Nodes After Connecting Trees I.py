There exist two undirected trees with n and m nodes, with distinct labels in ranges [0, n - 1] and [0, m - 1], respectively.
You are given two 2D integer arrays edges1 and edges2 of lengths n - 1 and m - 1, respectively, where edges1[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the first tree and edges2[i] = [ui, vi] indicates that there is an edge between nodes ui and vi in the second tree. You are also given an integer k.
Node u is target to node v if the number of edges on the path from u to v is less than or equal to k. Note that a node is always target to itself.
Return an array of n integers answer, where answer[i] is the maximum possible number of nodes target to node i of the first tree if you have to connect one node from the first tree to another node in the second tree.

Note that queries are independent from each other. That is, for every query you will remove the added edge before proceeding to the next query.
#code here
 class Solution:
    def bfs(self, start: int, adj: List[List[int]], max_depth: int) -> set:
        visited = set()
        queue = deque([(start, 0)])
        visited.add(start)

        while queue:
            node, depth = queue.popleft()
            if depth == max_depth:
                continue
            for neighbor in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, depth + 1))
        return visited

    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        n1 = max(max(u, v) for u, v in edges1) + 1
        n2 = max(max(u, v) for u, v in edges2) + 1

        if k == 0:
            return [1] * n1
       
        adj1 = [[] for _ in range(n1+1)]
        adj2 = [[] for _ in range(n2+1)]

        for u, v in edges1:
            adj1[u].append(v)
            adj1[v].append(u)

        for u, v in edges2:
            adj2[u].append(v)
            adj2[v].append(u)

        mydist1=[]
        mydist2=0
        for i in range(n1):
            reachable_from_adj1 = self.bfs(i, adj1, k)
            mydist1.append(len(reachable_from_adj1))

        for i in range(n2):
            reachable_from_adj2 = self.bfs(i, adj2, k-1)
            mydist2 = max(mydist2,len(reachable_from_adj2))

        return [mydist2+i for i in mydist1]
        
        
