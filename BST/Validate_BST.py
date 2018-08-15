class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        nodeVal = self.inorderTraversal(root)
        for i in range(len(nodeVal) - 1):
            if nodeVal[i] >= nodeVal[i + 1]:
                return False
        return True

    def inorderTraversal(self, root):
        reslt = []
        if root:
            reslt = reslt + self.inorderTraversal(root.left)
            reslt.append(root.val)
            reslt = reslt + self.inorderTraversal(root.right)
        return reslt


if __name__ == "__main__":
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    a.left, a.right = b, c
    b.left, b.right = d, e
    reslt = Solution().isValidBST(a)
    print(reslt)