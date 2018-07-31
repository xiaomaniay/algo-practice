class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        reslt = []
        if root:
            # if root.left:
            #     reslt += self.inorderTraversal(root.left)
            # reslt.append(root.val)
            # if root.right:
            #     reslt += self.inorderTraversal(root.right)
            stack = []
            while root or stack:
                if root:
                    stack.append(root)
                    root = root.left
                else:
                    root = stack.pop()
                    reslt.append(root.val)
                    root = root.right
        return reslt





if __name__ == "__main__":
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    a.left, a.right = b, c
    b.left, b.right = d, e
    reslt = Solution().inorderTraversal(a)
    print(reslt)