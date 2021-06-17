"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        deque = collections.deque([root])
        
        while deque:
            size = len(deque)
            # prev = Node(None)
            for i in range(size):
                curr = deque.popleft()
                if i < size - 1:
                    curr.next = deque[0]
                if curr.left:
                    deque.append(curr.left)
                if curr.right:
                    deque.append(curr.right)
        return root
