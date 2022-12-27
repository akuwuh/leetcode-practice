# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """"
        current = head
        len = 0
        while(current): 
            len+=1
            current = current.next

        if len == n: 
            return head.next

        current = head
        counter = len - n

        i = 0    
        while(current):
            if i == counter - 1: #at node before node to remove
                temp = current.next #pointer to node to remove
                current.next = temp.next 
                temp.next = None
                temp = None


            i +=1
            current = current.next
            
        """
        
        dummy = ListNode(0, head)
        left = dummy
        right = head 
        
        while n > 0 and right:
            right = right.next
            n-=1
            
        while right:
            left = left.next
            right = right.next
        
        left.next = left.next.next
        
        return dummy.next 