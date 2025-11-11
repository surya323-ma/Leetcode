You are given an array of integers nums and the head of a linked list. Return the head of the modified linked list after removing all nodes from the linked list that have a value that exists in nums.

 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        to_remove = set(nums)  # Convert to set for O(1) lookups
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        while current and current.next:
            if current.next.val in to_remove:
                current.next = current.next.next  # Skip the node
            else:
                current = current.next

        return dummy.next
