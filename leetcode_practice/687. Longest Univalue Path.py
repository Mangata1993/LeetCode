# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)  #longest univalue path in the left subtree
            right = dfs(node.right)         
            left_arrow = right_arrow = 0
            if node.left and node.left.val == node.val:
                left_arrow = left + 1
            if node.right and node.right.val == node.val:
                right_arrow = right + 1
            self.res = max(self.res, left_arrow + right_arrow)
            return max(left_arrow, right_arrow)
    
        dfs(root)
        return self.res
