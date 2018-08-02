class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        pre = None
        while root:
            if root.val == p.val:
                return root.right or pre
            else:
                if root.val < p.val:
                    root = root.right
                else:
                    pre = root
                    root = root.left
        return None


if __name__ == "__main__":
    a = TreeNode(4)
    b = TreeNode(2)
    c = TreeNode(5)
    d = TreeNode(1)
    e = TreeNode(3)
    a.left, a.right = b, c
    b.left, b.right = d, e
    reslt = Solution().inorderSuccessor(a, 1)
    print(reslt)