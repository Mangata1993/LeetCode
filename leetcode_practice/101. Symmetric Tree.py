# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
# method 1: recursive
#         def ismirror(r1, r2):
#             if not r1 and not r2:
#                 return True
#             if not r1 or not r2:
#                 return False
#             return r1.val == r2.val and ismirror(r1.left, r2.right) and ismirror(r1.right, r2.left)
        
#         return ismirror(root.left, root.right)

# method 2: iterative 
        if not root:
            return True
        queue = collections.deque()
        queue.extend([root.left, root.right])
        print(queue)
        while queue:
            left, right = queue.popleft(), queue.popleft()
            if not left and not right:
                continue
            elif (not left or not right) or left.val != right.val:
                return False
            queue += [left.left, right.right, left.right, right.left]
        return True
    
