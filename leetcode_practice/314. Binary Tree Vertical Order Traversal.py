# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        # colmap = collections.defaultdict(list)
        # # queue = [node.val, colidx]
        # queue = deque([(root, 0)])
        # while queue:
        #     node, colidx = queue.popleft()
        #     if node:
        #         colmap[colidx].append(node.val)
        #         queue.append((node.left, colidx - 1))
        #         queue.append((node.right, colidx + 1))
        # res = []
        # # for key in sorted(colmap.keys()):
        # #     res.append(colmap[key])
        # return [colmap[key] for key in sorted(colmap.keys())]
        def helper(node, rowidx, colidx):
            if not node:
                return
            
            
            helper(node.left, rowidx + 1, colidx - 1)
            colmap[colidx].append((rowidx, node.val))
            self.mincol = min(self.mincol, colidx)
            self.maxcol = max(self.maxcol, colidx)
            helper(node.right, rowidx + 1, colidx + 1)
            return colmap
        
        if root is None:
            return []
        colmap = collections.defaultdict(list)
        self.mincol, self.maxcol = 0, 0
        helper(root, 0, 0)
        for i in range(self.mincol, self.maxcol + 1):
            colmap[i].sort(key = lambda x: x[0])
        return [[val for row, val in colmap[i]] for i in range(self.mincol, self.maxcol + 1) ]
