# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # if not root:
        #     return
        def dfs(node):
            if not node:
                return
            if not node.left and not node.right:
                return node
            # node.right = node.left
            # node.left = None
            leftnode = dfs(node.left)
            rightnode = dfs(node.right)
            if leftnode:
                leftnode.right = node.right
                node.right = node.left
                node.left = None
            return rightnode if rightnode else leftnode
        dfs(root)
