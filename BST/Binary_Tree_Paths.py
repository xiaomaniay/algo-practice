class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def binaryTreePaths(self, root):
        paths = []
        if root:
            paths = self.binaryTreePaths(root.left) + self.binaryTreePaths(root.right)
            if paths:
                for i, path in enumerate(paths):
                    paths[i] = str(root.val) + "->" + path
            else:
                paths.append(str(root.val))
        return paths


if __name__ == "__main__":
    a = TreeNode(4)
    b = TreeNode(2)
    c = TreeNode(5)
    d = TreeNode(1)
    e = TreeNode(3)
    a.left, a.right = b, c
    b.left, b.right = d, e
    reslt = Solution().binaryTreePaths(a)
    print(reslt)