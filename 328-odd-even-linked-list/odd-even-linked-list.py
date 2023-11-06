# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head: return None

        # evennode = False
        even_node_head = ListNode()
        current_even_node = even_node_head
        current_odd_Node = head

        while current_odd_Node.next:
            current_even_node.next = current_odd_Node.next
            current_even_node = current_even_node.next
            if current_odd_Node.next.next:
                current_odd_Node.next = current_odd_Node.next.next
                current_odd_Node = current_odd_Node.next
            else: break
        
        current_odd_Node.next = even_node_head.next
        current_even_node.next = None

        return head
