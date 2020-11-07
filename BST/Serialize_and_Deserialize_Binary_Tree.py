import collections

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """
    def serialize(self, root):
        serialized = []

        def preorder(root):
            if root:
                serialized.append(root.val)
                preorder(root.left)
                preorder(root.right)
            else:
                serialized.append('#')

        preorder(root)
        serialized.pop()

        return '{' + ','.join(str(x) for x in serialized) + '}'

    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in
    "serialize" method.
    """
    def deserialize(self, data):
        nodes = collections.deque([x for x in data[1: -1].split(',')])
        if not nodes:
            return TreeNode(None)

        def build(nodes):
            if nodes:
                val = nodes.popleft()
                if val is not '#':
                    root = TreeNode(val)
                    root.left = build(nodes)
                    root.right = build(nodes)
                    return root
            else:
                return None

        return build(nodes)


root = Solution().deserialize('{3,9,#,#,20,15,7}')
print(Solution().serialize(root))