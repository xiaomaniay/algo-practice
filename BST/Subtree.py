class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param T1: The roots of binary tree T1.
    @param T2: The roots of binary tree T2.
    @return: True if T2 is a subtree of T1, or false.
    """
    def isSubtree(self, T1, T2):
        if not T2:
            return True
        if T1:
            checkRoot = self.isIdentical(T1, T2)
            if checkRoot:
                return True
            checkLeft = self.isSubtree(T1.left, T2)
            checkRight = self.isSubtree(T1.right, T2)
            if checkLeft or checkRight:
                return True
        return False

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
    a.left, a.right = b, c
    c.left = d
    reslt = Solution().isSubtree(a, c)
    print(reslt)
