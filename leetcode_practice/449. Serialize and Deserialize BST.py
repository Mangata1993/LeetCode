# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        vals = []
        def preorder(node):
            if node:
                vals.append(node.val)
                preorder(node.left)
                preorder(node.right)
        
        preorder(root)
        return ' '.join(map(str, vals))

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        vals = collections.deque(int(i) for i in data.split())
        def build(low, high):
            if vals and low < vals[0] < high:
                val = vals.popleft()
                node = TreeNode(val)
                node.left = build(low, val)
                node.right = build(val, high)
                return node
        return build(float('-inf'), float('inf'))

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
