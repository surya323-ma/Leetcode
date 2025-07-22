Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
class Solution:
    def sortedArrayToBST (self, nums: List[int]) ->Optional [TreeNode]:
        def buildBST(nums,l,r):
            if l>r:
                return None
            mid = (l+r)//2
            root= TreeNode(nums[mid])
            root.left=buildBST (nums, l, mid-1)
            root.right=buildBST (nums, mid+1, r)
            return root
        return buildBST (nums, 0, len(nums)-1)
