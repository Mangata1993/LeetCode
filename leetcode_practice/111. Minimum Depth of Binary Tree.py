# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        deque = collections.deque([(1, root)])
        while deque:
            depth, node = deque.popleft()
            children = [node.left, node.right]
            if not any(children):
                return depth
            for c in children:
                if c:
                    deque.append((depth + 1, c))
                    
