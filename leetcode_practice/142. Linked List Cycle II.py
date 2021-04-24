# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while fast and fast.next:
            if slow == fast:
                node2 = slow
            else:
                slow = slow.next
                fast = fast.next.next
        return None
    
        node1, node2 = head, slow
        if node1 != node2:
            node1 = node1.next
            node2 = node2.next
        return node1
        
    # slow = fast = head            #这样连等是可以的吗？
    # while fast and fast.next:
    #     slow = slow.next
    #     fast = fast.next.next
    #     if slow == fast:
    #         break
    # else:
    #     return None
    # while head != slow:
    #     slow = slow.next
    #     head = head.next
    # return head
