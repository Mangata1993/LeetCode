# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        def countsum(node):
            if not node:
                return 0
            subsum = node.val + countsum(node.left) + countsum(node.right)
            count[subsum] += 1
            return subsum           #这句话没太明白，为什么是return这个而不是count。把当前的sum返回给父节点
        
        count = collections.Counter()
        countsum(root)
        maxcnt = max(count.values())            
        return [num for num in count if count[num] == maxcnt]
    
    
