# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)     #the excess number of coins
            right = dfs(node.right)
            self.res += abs(left) + abs(right)
            return node.val + left + right - 1
        
        dfs(root)
        return self.res
