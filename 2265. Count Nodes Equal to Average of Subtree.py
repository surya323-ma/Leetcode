Given the root of a binary tree, return the number of nodes where the value of the node is equal to the average of the values in its subtree.

Note:

The average of n elements is the sum of the n elements divided by n and rounded down to the nearest integer.
A subtree of root is a tree consisting of root and all of its descendants.
 # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(node):
            if not node: return (0,0)
            s1,c1 = dfs(node.left)
            s2,c2 = dfs(node.right)
            total, cnt = s1+s2+node.val, c1+c2+1
            if node.val == total//cnt: self.res += 1
            return (total,cnt)
        dfs(root)
        return self.res
        
        
