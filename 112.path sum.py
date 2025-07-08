Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return targetSum == root.val
        return (self.hasPathSum(root.left, targetSum - root.val) or
                self.hasPathSum(root.right, targetSum - root.val))


using helper 
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def helper(x,target,sum):
            if not x:
                return False
            if x and not x.left and not x.right:
                sum=sum+x.val
            if sum==target:
                return True
            return helper(x.left,target,sum+x.val) or helper(x.right,target,sum+x.val)
            return helper(root,targetsum,0)
   

