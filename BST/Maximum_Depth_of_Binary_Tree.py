class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: The root of binary tree
    @return: An integer
    """
    def maxDepth(self, root):
        if not root:
            return 0
        else:
            leftMinDepth = self.maxDepth(root.left)
            rightMinDepth = self.maxDepth(root.right)
            depth = 1 + max(leftMinDepth, rightMinDepth)
            return depth


if __name__ == "__main__":
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(1)
    f = TreeNode(2)
    g = TreeNode(3)
    h = TreeNode(4)
    a.left, a.right = b, c
    b.left = d
    e.left, e.right = f, g
    f.left = h
    reslt = Solution().minDepth(a)
    print(reslt)
