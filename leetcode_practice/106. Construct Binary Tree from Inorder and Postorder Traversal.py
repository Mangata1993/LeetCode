# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        idx = {}
        for i, val in enumerate(inorder):
            idx[val] = i
        if inorder:
            val = postorder.pop()
            root = TreeNode(val)
            root.right = self.buildTree(inorder[idx[val]+1:], postorder)
            root.left = self.buildTree(inorder[:idx[val]], postorder)
            return root
