# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        len = 0
        current = head
        
        while (current):
            len+=1
            current = current.next
        
        counter = int(len/2) 
        
        current = head
        i = 0
        while(current): 
            if i == counter:
                return current
            
            i+=1
            current = current.next
        
        return current
    