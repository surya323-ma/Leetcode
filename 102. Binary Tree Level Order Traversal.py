Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque([root])
        li = []

        while q:
            li.append([x.val for x in q])
            for _ in range(len(q)):
                popped = q.popleft()
                if popped.left:
                    q.append(popped.left)
                if popped.right:
                    q.append(popped.right)
        return li
