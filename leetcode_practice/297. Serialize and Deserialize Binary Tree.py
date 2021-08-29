# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        res = []
        # queue = [root]
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            if not node:
                res.append('null')
                continue
            res.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
        return ','.join(res)
    
    # def deserialize (self, data):
#         if not data: return None
#         nodes = data.split(',')
#         root = TreeNode(int(nodes[0]))
#         q = collections.deque([root])
#         index = 1
#         while q:
#             node = q.popleft()
#             if nodes[index] is not '#':
#                 node.left = TreeNode(int(nodes[index]))
#                 q.append(node.left)
#             index += 1
        
#             if nodes[index] is not '#':
#                 node.right = TreeNode(int(nodes[index]))
#                 q.append(node.right)
#             index += 1
#         return root

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        lst = data.split(',')
        root = TreeNode(int(lst[0]))
        queue = collections.deque()
        queue.append(root)
        i = 1
        while queue:
            node = queue.popleft()
            if lst[i] != 'null':
                left = TreeNode(int(lst[i]))
                node.left = left
                queue.append(left)
            i += 1
            if lst[i] != 'null':
                right = TreeNode(int(lst[i]))
                node.right = right
                queue.append(right)
            i += 1
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
