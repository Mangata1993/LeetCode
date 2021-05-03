# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        def findpar(node, par):
            if node:
                node.par = par
                findpar(node.left, node)
                findpar(node.right, node)
        findpar(root, None)
        
        queue = [(target, 0)]
        res = []
        seen = {target}
        while queue:
            node, dist = queue.pop()
            if dist == K:
                res.append(node.val)
            for n in (node.left, node.right, node.par):
                if n and n not in seen:
                    queue.append((n, dist + 1))
                    seen.add(n)
        return res
