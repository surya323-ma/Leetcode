You are given a directed graph of n nodes numbered from 0 to n - 1, where each node has at most one outgoing edge.
The graph is represented with a given 0-indexed array edges of size n, indicating that there is a directed edge from node i to node edges[i]. If there is no outgoing edge from i, then edges[i] == -1.
You are also given two integers node1 and node2.
Return the index of the node that can be reached from both node1 and node2, such that the maximum between the distance from node1 to that node, and from node2 to that node is minimized. If there are multiple answers, return the node with the smallest index, and if no possible answer exists, return -1.

Note that edges may contain cycles.
  #code here
  

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def bfs(start):
            n = len(edges)
            dist = [-1] * n  # Initialize all distances as -1
            queue = deque([start])
            dist[start] = 0 
            while queue:
                node = queue.popleft()
                next_node = edges[node]
                if next_node != -1 and dist[next_node] == -1:
                    dist[next_node] = dist[node] + 1
                    queue.append(next_node)
            return dist
        dist1 = bfs(node1)
        dist2 = bfs(node2)
        min_distance = float('inf')
        result = -1
        for i in range(len(edges)):
            if dist1[i] != -1 and dist2[i] != -1:
                max_dist = max(dist1[i], dist2[i])
                if max_dist < min_distance:
                    min_distance = max_dist
                    result = i
        return result
