# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        paths = []
        def traverse(node, cursum, path):
            if node:
                cursum += node.val
                path += [node.val]
                if not node.left and not node.right and cursum == targetSum:
                    # path += [node.val]
                    paths.append(list(path))
                else:
                    # traverse(node.left, cursum + node.val, path + [node.val])
                    # traverse(node.right, cursum + node.val, path + [node.val])
                    traverse(node.left, cursum, path)
                    traverse(node.right, cursum, path)
                path.pop()
                
        traverse(root, 0, [])
        return paths
