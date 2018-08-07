class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param: A: an integer array
    @return: A tree node
    """
    def sortedArrayToBST(self, A):
        if not A:
            return None
        midIndx = int((len(A) - 1) / 2)
        mid = A[midIndx]
        leftA = A[0: midIndx]
        rightA = A[(midIndx + 1):]
        root = TreeNode(mid)
        root.left = self.sortedArrayToBST(leftA)
        root.right = self.sortedArrayToBST(rightA)
        return root


if __name__ == "__main__":
    a = [1,2,3,4,5,6,7,8]
    test = Solution()
    reslt = test.sortedArrayToBST(a)
    print(reslt)