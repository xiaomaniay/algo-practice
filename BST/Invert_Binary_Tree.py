"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    # def invertBinaryTree(self, root):
    #     if root:
    #         self.invert(root)
    #
    # def invert(self, root):
    #     if root:
    #         root.left, root.right = self.invert(root.right), self.invert(root.left)
    #     return root
    """Iterative method"""
    def invertBinaryTree(self, root):
        stack = []
        while root or stack:
            if root:
                root.left, root.right = root.right, root.left
                stack.append(root.right)
                root = root.left
            else:
                root = stack.pop()
