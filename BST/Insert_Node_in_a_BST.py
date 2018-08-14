class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: node: insert this node into the binary search tree
    @return: The root of the new binary search tree.
    """
    def insertNode(self, root, node):
        if not root:
            return node
        if root.val > node.val:
            root.left = self.insertNode(root.left, node)
        else:
            root.right = self.insertNode(root.right, node)
        return root


if __name__ == "__main__":
    a = TreeNode(10)
    b = TreeNode(9)
    c = TreeNode(8)
    d = TreeNode(7)
    e = TreeNode(4)
    f = TreeNode(6)
    g = TreeNode(5)
    a.left = b
    b.left = c
    c.left = d
    d.left = e
    e.right = f
    reslt = Solution().insertNode(a, 5)
    print(reslt)
