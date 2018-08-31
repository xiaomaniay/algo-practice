class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param: : the root of tree
    @param: : the target sum
    @return: two numbers from tree which sum is n
    """
    def twoSum(self, root, n):
        if not root:
            return None
        curr = root
        return self.check(root, curr, n)

    def check(self, root, curr, n):
        if not root:
            return None
        if self.search(root, n - curr.val):
            return [curr.val, n - curr.val]
        else:
            return self.check(root, curr.left, n) or self.check(root, curr.right, n)

    def search(self, root, target):
        if not root:
            return False
        while root:
            if root.val == target:
                return True
            elif root.val > target:
                root = root.left
            else:
                root = root.right
        return False


if __name__ == "__main__":
    a = TreeNode(4)
    b = TreeNode(2)
    c = TreeNode(5)
    d = TreeNode(1)
    e = TreeNode(3)
    a.left, a.right = b, c
    b.left, b.right = d, e
    reslt = Solution().twoSum(a, 3)
    print(reslt)