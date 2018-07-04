"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: the root of tree
    @return: the max node
    """

    def maxNode(self, root):

        if not root:
            return None

        globMax = root

        leftMax = self.maxNode(root.left)
        rightMax = self.maxNode(root.right)

        if leftMax:
            if leftMax.val > globMax.val:
                globMax = leftMax
        if rightMax:
            if rightMax.val > globMax.val:
                globMax = rightMax

        return globMax