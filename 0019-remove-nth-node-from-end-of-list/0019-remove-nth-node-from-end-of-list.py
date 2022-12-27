# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        len = 0
        while(current): 
            len+=1
            current = current.next

        if len == 1:
            head = None 
            return head

        if len == n: 
            temp = head
            head = temp.next
            temp.next = None
            temp = None

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

        return head 