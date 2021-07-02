# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        nodes = [(l.val, idx) for idx, l in enumerate(lists) if l]
        heapq.heapify(nodes)
        dummy = head = ListNode(0)
        while nodes:
            val, idx = heapq.heappop(nodes)
            head.next = ListNode(val)
            head = head.next
            lists[idx] = lists[idx].next
            if lists[idx]:
                heapq.heappush(nodes, (lists[idx].val, idx))
        
        return dummy.next
            
            
