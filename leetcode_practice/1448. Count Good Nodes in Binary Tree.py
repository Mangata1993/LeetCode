# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def helper(node, maxnum):
            if not node:
                return
            if node.val >= maxnum:
                self.count += 1
            maxnum = max(maxnum, node.val)
            helper(node.left, maxnum)
            helper(node.right, maxnum)
        
        self.count = 0
        helper(root, float('-inf'))
        return self.count
    
#         def dfs(node, max_so_far):
#             nonlocal num_good_nodes
#             if max_so_far <= node.val:
#                 num_good_nodes += 1
#             if node.right:
#                 dfs(node.right, max(node.val, max_so_far))
#             if node.left:
#                 dfs(node.left, max(node.val, max_so_far))
        
#         num_good_nodes = 0
#         dfs(root, float("-inf"))
#         return num_good_nodes
            
            