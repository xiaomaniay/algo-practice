
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        reslt = []

        if root:
            reslt.append(root.val)
            if root.left:
                reslt += self.preorderTraversal(root.left)
            if root.right:
                reslt += self.preorderTraversal(root.right)
        return reslt
        # stack = []
        # while root or stack:
        #     if root:
        #         reslt.append(root.val)
        #         stack.append(root)
        #         root = root.left
        #     else:
        #         root = stack.pop()
        #         root = root.right
        # return reslt


if __name__ == "__main__":
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    a.left, a.right = b, c
    b.left, b.right = d, e
    reslt = Solution().preorderTraversal(a)
    print(reslt)


