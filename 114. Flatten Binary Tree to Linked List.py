The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
       current root
       while current:
            if current.left:
                predecessor= current.left
                while predecessor.right:
                    predecessor =predecessor.right
                predecessor.right=current.right
                current.right=current.left
                current.left = None
            current=current.right
