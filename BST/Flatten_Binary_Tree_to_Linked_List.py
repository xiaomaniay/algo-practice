class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def flatten(self, root):
        leftRoot = rightRoot = None
        if root:
            if root.right:
                rightRoot = self.flatten(root.right)
            if root.left:
                leftRoot = self.flatten(root.left)
                root.right = leftRoot
                while leftRoot.right:
                    leftRoot = leftRoot.right
                leftRoot.right = rightRoot
                root.left = None
        return root

if __name__ == "__main__":
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    a.left, a.right = b, c
    b.left, b.right = d, e
    reslt = Solution().flatten(a)
    print(reslt)