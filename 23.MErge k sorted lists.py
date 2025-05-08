You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
#code here
 #Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        main_heap=[]
        for i in range(len(lists)): 
            if lists[i]: 
                heappush(main_heap, (lists[i].val, i, lists[i])) 
        dummy = ListNode(0) 
        current = dummy 
        while main_heap: 
            val, i, node = heappop(main_heap) 
            current.next = ListNode(val) 
            current = current.next 
            if node.next: 
                heappush(main_heap, (node.next.val, i, node.next)) 
        return dummy.next  
