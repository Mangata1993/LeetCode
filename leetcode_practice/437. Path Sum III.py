#法一 DFS (brute force)双递归：外层递归保证遍历到树的所有节点；内层递归才是真正寻找当前节点的递归 -- 以当前节点为根节点，路径和符合要求的情况
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        # self.res = 0
        def dfs(root, cursum, res):
                # print(root)
            if not root:
                return
            if cursum + root.val == targetSum:
                # print(self.res)
                self.res += 1
            dfs(root.left, cursum + root.val, self.res)
            dfs(root.right, cursum + root.val, self.res)

        def helper(root):
            if not root:
                return
            dfs(root, 0, self.res)
            helper(root.left)
            helper(root.right)
                    
        self.res = 0
        helper(root)
        return self.res
      
#法二 Prefix
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        h = defaultdict(int)
        self.count = cursum = 0
        def preorder(root, cursum):
            if not root:
                return 0
            cursum += root.val
            if cursum == targetSum:
                self.count += 1
            self.count += h[cursum - targetSum]
            h[cursum] += 1
            preorder(root.left, cursum)
            preorder(root.right, cursum)
            # cursum -= root.val
            h[cursum] -= 1          #为什么是减dictionary里的count而不是减cursum
            
        preorder(root, 0)
        return self.count
        
