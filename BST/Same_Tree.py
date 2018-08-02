class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param a: the root of binary tree a.
    @param b: the root of binary tree b.
    @return: true if they are identical, or false.
    """
    def isIdentical(self, a, b):
        if not (a or b):
            return True
        stackA, stackB = [], []
        while a or b or stackA or stackB:
            if a and b:
                if a.val != b.val:
                    return False
                stackA.append(a)
                stackB.append(b)
                a, b = a.left, b.left
            elif not (a or b):
                a, b = stackA.pop(), stackB.pop()
                a, b = a.right, b.right
            else:
                return False
        return True


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
    reslt = Solution().isIdentical(a, h)
    print(reslt)




