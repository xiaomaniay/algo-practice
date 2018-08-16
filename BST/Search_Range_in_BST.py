class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """
    def searchRange(self, root, k1, k2):
        reslt = []
        if root:
            reslt = reslt + self.searchRange(root.left, k1, k2)
            if k1 <= root.val <= k2:
                reslt.append(root.val)
            reslt = reslt + self.searchRange(root.right, k1, k2)
        return reslt


if __name__ == "__main__":
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    a.left, a.right = b, c
    b.left, b.right = d, e
    reslt = Solution().searchRange(a, 2, 5)
    print(reslt)
