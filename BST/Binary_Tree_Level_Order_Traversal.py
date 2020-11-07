class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """

    def levelOrder(self, root):
        depth, reslt = 0, []
        self.bfs(root, reslt, depth)
        return reslt

    def bfs(self, root, reslt, depth):
        if root:
            if len(reslt) < depth + 1:
                reslt.append([])
            reslt[depth].append(root.val)
            self.bfs(root.left, reslt, depth + 1)
            self.bfs(root.right, reslt, depth + 1)


if __name__ == "__main__":
    a = TreeNode(10)
    b = TreeNode(9)
    c = TreeNode(8)
    d = TreeNode(7)
    e = TreeNode(4)
    f = TreeNode(6)
    a.left = b
    b.left = c
    c.left = d
    d.left = e
    e.right = f
    reslt = Solution().levelOrder(a)
    print(reslt)