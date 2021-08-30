# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
#         n = len(preorder)
        
#         def helper(lower, upper):
#             if self.idx == n:
#                 return
#             val = preorder[self.idx]
#             if val < lower or val > upper:
#                 return
#             root = TreeNode(val)
#             self.idx += 1
#             root.left = helper(lower, val)
#             root.right = helper(val, upper)
#             return root
        
#         self.idx = 0
#         return helper(float('-inf'), float('inf'))
        
        
        root = TreeNode(preorder[0])
        stack = [root]
        for i in range(1, len(preorder)):
            parent = stack[-1]
            child = TreeNode(preorder[i])
            while stack and stack[-1].val < child.val:
                parent = stack.pop()
            if parent.val < child.val:
                parent.right = child
            else:
                parent.left = child
            stack.append(child)
        return root
            
