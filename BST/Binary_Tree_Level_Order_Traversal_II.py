class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: A tree
    @return: buttom-up level order a list of lists of integer
    """
    def levelOrderBottom(self, root):
        p = [root]
        reslt = []
        while p:
            newP = []
            newReslt = []
            for i in range(len(p)):
                if p[i]:
                    newP.append(p[i].left)
                    newP.append(p[i].right)
                    newReslt.append(p[i].val)
            p = newP
            if len(newReslt) > 0:
                reslt.insert(0, newReslt)
        return reslt


if __name__ == "__main__":
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    a.left, a.right = b, c
    b.left, b.right = d, e
    reslt = Solution().levelOrderBottom(a)
    print(reslt)

