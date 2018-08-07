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
            sameValueNode = self.findT2Value(T1, T2)
            for node in sameValueNode:
                isIdentical = self.isIdentical(node, T2)
                if isIdentical:
                    return True
        return False

    def findT2Value(self, T1, T2):
        sameValueNode = []
        if T1:
            if T1.val == T2.val:
                sameValueNode.append(T1)
            leftNode = self.findT2Value(T1.left, T2)
            rightNode = self.findT2Value(T1.right, T2)
            sameValueNode = sameValueNode + leftNode + rightNode
        return sameValueNode

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
