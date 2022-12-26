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
        ret = ListNode()
        currnew = ret
        
        while(current): 
            if i == counter:
                ret.val = current.val
                ret.next= None  
            if i > counter:
                new = ListNode(current.val, None)
                currnew.next = new
                currnew = currnew.next
            
            current = current.next
            i+=1
                
            
        
        return ret
    