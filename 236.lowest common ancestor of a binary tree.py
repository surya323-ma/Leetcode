Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

#code here

from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        parents = {root: None}
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node.left:
                parents[node.left] = node
                queue.append(node.left)
            if node.right:
                parents[node.right] = node
                queue.append(node.right)
        path_p = []
        while p:
            path_p.append(p)
            p = parents[p]

        path_q = []
        while q:
            path_q.append(q)
            q = parents[q]
        path_p.reverse()
        path_q.reverse()

        lca = None
        for u, v in zip(path_p, path_q):
            if u == v:
                lca = u
            else:

                break

        return lca






