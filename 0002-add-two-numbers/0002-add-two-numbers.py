# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(0, None)
        remainder = 0
        curr = ans 
        while l1 or l2:
            s = 0
            if l1 and l2: s = l1.val + l2.val + remainder
            elif l1:
                s = l1.val + remainder
            elif l2: 
                s = l2.val + remainder
            remainder = 0
            if s >= 10: # needs to update remainder
                remainder = s//10
                s = s%10
                
            curr.next = ListNode(s, None)
            curr = curr.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        if remainder > 0: 
            curr.next = ListNode(remainder, None)
        
    
        return ans.next
        