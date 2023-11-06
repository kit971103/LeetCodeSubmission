# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        
        
        current = head.next
        head_reversed = head
        head_reversed.next = None

        while current.next:
            temp = current.next
            current.next = head_reversed
            head_reversed = current
            current = temp
        
        current.next = head_reversed

        return current

        