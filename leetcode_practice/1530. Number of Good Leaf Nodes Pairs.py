# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.res = 0
        def caldist(root):
            if not root:
                return []
            if not root.left and not root.right:
                return [1]
            left = caldist(root.left)
            right = caldist(root.right)
            
            # for i in left:
            #     for j in right:
            #         if i + j <= distance:
            #             self.res += 1
            self.res += sum(l + r <= distance for l in left for r in right)
            for n in left + right:
                if n + 1 < distance:
                    return [n + 1]
        
        caldist(root)
        return self.res
        
#         count = 0
#         def dfs(node):
#             nonlocal count
#             if not node:
#                 return []
#             if not node.left and not node.right:
#                 return [1]
#             left = dfs(node.left)
#             right = dfs(node.right)
#             count += sum(l + r <= distance for l in left for r in right)
#             return [n + 1 for n in left + right if n + 1 < distance]
#         dfs(root)
#         return count
    
