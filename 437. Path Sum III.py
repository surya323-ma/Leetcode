Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node,current_sum):
            if not node:
                return 0
            current_sum +=node.val
            count = prefix_sums.get(current_sum - targetSum,0)

            prefix_sums[current_sum]=prefix_sums.get(current_sum,0)+1
            count+=dfs(node.left,current_sum)
            count+=dfs(node.right,current_sum)
            prefix_sums[current_sum]-=1
            return count
        prefix_sums={0:1}
        return dfs(root,0)
