# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None)
        dummy.next = head
        prev = dummy
        curr = head
        
        seen = {}
        
        while curr:
            if (curr.next != None and curr.val == curr.next.val) or curr.val in seen: # if  duplicate. 
                                                              # conditions:
                                                              # first duplicate: next node is same as current node
                                                              # or
                                                              # seen before: curr node is in seen
                prev.next = curr.next #remove by connecting prev to next 
                seen[curr.val] = 0 # add to dict if first duplicate 
                curr = curr.next # update curr to move on to next but don't update prev
                continue
            
            #else no need to remove
            
            seen[curr.val] = 0 # add to dict regardless of whether seen or not cuz it'll just override
            curr = curr.next #update curr to next node
            prev = prev.next #update prev to next node only when when 
            
        return dummy.next
            
            # 1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5
            #      p    c
            #      p ------> 3 example of curr.val == curr.next.val 
            # 1 -> 2 -> 3 -> 4 -> 4 -> 5
            #      p    c
            #      p ------> 4
            # 1 -> 2 -> 4 -> 4 -> 5
            #      p    c 
            #      p ------> 4
            # 1 -> 2 -> 4 -> 5
            #      p    c
            #      p ------> 5
            # 1 -> 2 -> 5
            #      p    c 
                
            