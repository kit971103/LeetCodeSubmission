# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        listVal = [head.val]
        while head.next:
            head = head.next
            listVal.append(head.val)
        
        max_twin_sum = 2
        n = len(listVal)
        for i in range(n//2):
            twin_sum = listVal[i] + listVal[n-1-i]
            if twin_sum > max_twin_sum: max_twin_sum = twin_sum
        return max_twin_sum
        
        