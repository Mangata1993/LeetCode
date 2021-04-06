# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        idx = {}
        for i, val in enumerate(inorder):
            idx[val] = i
        if inorder:
            val = preorder.pop(0)
            root = TreeNode(val)
            # idx = inorder.index(root.val)
            root.left = self.buildTree(preorder, inorder[:idx[val]])
            root.right = self.buildTree(preorder, inorder[idx[val]+1:])
            return root
        
