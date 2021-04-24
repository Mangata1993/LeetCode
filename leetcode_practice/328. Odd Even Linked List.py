# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        list1 = ListNode(0)                     #list1 = head
        list2 = ListNode(0)                     #list2 = head.next
        tmp1 = list1
        tmp2 = list2
        adj = 1                                 #adj = 3
        while head:
            if adj % 2 == 1:
                list1.next = head
                list1 = list1.next
            else:
                list2.next = head
                list2 = list2.next
            head = head.next
            adj += 1
        list2.next = None                   #为什么不加这句会以为是环
        list1.next = tmp2.next
        return tmp1.next
