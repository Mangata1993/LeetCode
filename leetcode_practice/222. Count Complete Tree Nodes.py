# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        def compute_depth(node):
            depth = 0
            while node.left:
                node = node.left
                depth += 1
            return depth
        
        def exist(idx, depth, node):
            left, right = 0, 2 ** depth - 1
            for i in range(depth):
                pivot = (left + right) // 2
                if idx <= pivot:
                    node = node.left
                    right = pivot
                else:
                    node = node.right
                    left = pivot
            return node is not None
        
        if not root:
            return 0
        d = compute_depth(root)
        if d == 0:
            return 1
        left, right = 0, 2 ** d - 1
        while left <= right:
            mid = (left + right) // 2
            if exist(mid, d, root):
                left = mid + 1
            else:
                right = mid - 1
        return 2 ** d - 1 + left
            
