Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

The most significant bit is at the head of the linked list.

class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        num = 0
        while head:
            num = (num << 1) | head.val
            head = head.next
        return num
