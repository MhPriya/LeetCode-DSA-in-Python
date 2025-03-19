# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)  # Dummy node to store result
        current = dummy
        carry = 0
        
        while l1 or l2 or carry:
            # Get values from nodes (0 if node is None)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Compute sum and carry
            total = val1 + val2 + carry
            carry = total // 10  # Update carry
            current.next = ListNode(total % 10)  # Store last digit
            
            # Move to the next nodes
            current = current.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        return dummy.next  # Return result list (excluding dummy)