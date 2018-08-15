class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: A Tree
    @return: A list of lists of integer include the zigzag level order traversal of its nodes' values.
    """
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        q = [root]
        order = 0
        reslt = []
        while q:
            level = []
            levelVal = []
            for i in range(len(q) -1, -1, -1):
                if q[i]:
                    levelVal.append(q[i].val)
                    if order == 0:
                        level.append(q[i].left)
                        level.append(q[i].right)
                    else:
                        level.append(q[i].right)
                        level.append(q[i].left)
            order = 1 if order == 0 else 0
            q = level
            if len(levelVal) > 0:
                reslt.append(levelVal)
        return reslt


if __name__ == "__main__":
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    a.left, a.right = b, c
    b.left, b.right = d, e
    reslt = Solution().zigzagLevelOrder(a)
    print(reslt)


