# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        def isBST(node, _min, _max):
            if not node:
                return True
            if node.val <= _min or node.val >= _max:
                return False
            return isBST(node.left, _min, node.val) and isBST(node.right, node.val, _max)
        
        def countnode(node):
            return 1 + countnode(node.left) + countnode(node.right) if node else 0
            
        if not root:
            return 0
        if isBST(root, float('-inf'), float('inf')):
            return countnode(root)
        return max(self.largestBSTSubtree(root.left), self.largestBSTSubtree(root.right))
            
       

#     def isBST(node,lower,upper): # return if a BT is a BST or not!
#         if not node:
#             return True
#         if node.val<=lower or node.val>=upper:
#             return False
#         else:
#             return isBST(node.left,lower,node.val) and isBST(node.right,node.val,upper)
  
    
#     lower = -float('inf')
#     upper = float('inf')
    
#     if isBST(root,lower,upper):
#         return size(root)
#     else:
#         return max(self.largestBSTSubtree(root.left),self.largestBSTSubtree(root.right))     
