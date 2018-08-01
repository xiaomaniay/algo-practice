class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        reslt = []
        if root:
            reslt += self.postorderTraversal(root.left)
            reslt += self.postorderTraversal(root.right)
            reslt.append(root.val)

            # stack = []
            # while root or stack:
            #     if root:
            #         stack.append(root)
            #         root = root.left
            #     else:
            #         root = stack.pop()
            #         if root.right:
            #             temp = root.right
            #             root.right = None
            #             stack.append(root)
            #             root = temp
            #         else:
            #             reslt.append(root.val)
            #             root = None
        return reslt


if __name__ == "__main__":
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    a.left, a.right = b, c
    b.left, b.right = d, e
    reslt = Solution().postorderTraversal(a)
    print(reslt)
