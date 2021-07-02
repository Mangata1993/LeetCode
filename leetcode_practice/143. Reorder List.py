# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        prev = None
        curr = slow
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
            
        first, second = head, prev
        # print(first, second)
        while second.next:            # 这边必须是while second.next。while first: second may be None; while second: first may be None
            tmp = first.next
            first.next = second
            first = tmp
            print(first)
            
            tmptwo = second.next
            second.next = first
            second = tmptwo
            print(second)
        return head
            
            
             
        
    
    
       
                
