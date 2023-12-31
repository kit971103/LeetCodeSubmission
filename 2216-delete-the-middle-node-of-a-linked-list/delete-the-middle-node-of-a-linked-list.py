# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head.next: return None

        inedx = 1
        current = head.next
        before_middle = head

        while current.next:
            current = current.next
            inedx+=1
            if inedx%2: before_middle = before_middle.next
        
        before_middle.next = before_middle.next.next

        return head
        


        