class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
class Solution:
    def pathSum(self, nums: List[int]) -> int:
        self.res = 0
        root = TreeNode(nums[0] % 10)
        # if not node:
        #     return
        for num in nums[1:]:
            depth, pos, val = num // 100, num // 10 % 10, num % 10
            pos -= 1
            cur = root
            for d in range(depth - 2, -1, -1):
                if pos < 2 ** d:
                    if cur.left:
                        cur = cur.left
                    else:
                        cur.left = TreeNode(val)
                else:
                    if cur.right:
                        cur = cur.right
                    else:
                        cur.right = TreeNode(val)
                pos = pos % (2 ** d)
                
        def dfs(node, running_sum):
            if not node:
                return
            running_sum += node.val
            if not node.left and not node.right:
                self.res += running_sum
            else:
                dfs(node.left, running_sum)
                dfs(node.right, running_sum)
                
        dfs(root, 0)
        return self.res
