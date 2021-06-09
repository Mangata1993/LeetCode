"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        stack, res = [root], []
        while stack:
            root = stack.pop()
            if root is not None:
                res.append(root.val)
            for node in root.children:
                stack.append(node)
        return res[::-1]
            
