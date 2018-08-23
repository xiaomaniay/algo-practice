class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: The root of binary tree.
    @return: The maximum amount of money you can rob tonight
    """
    def houseRobber3(self, root):
        if not root:
            return 0
        stack = []
        pre = curr = 0
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                if root.right:
                    temp = root.right
                    root.right = None
                    root = temp
                else:
                    temp = pre
                    pre = curr
                    curr = max(root.val + temp, curr)
                    root = None
        return curr

    # def houseRobber3(self, root):
    #     if not root:
    #         return 0
    #     if root.left:
    #         left_val = self.houseRobber3(root.left)
    #         left_pre = self.houseRobber3(root.left.left) + self.houseRobber3(root.left.right)
    #     else:
    #         left_val = left_pre = 0
    #     if root.right:
    #         right_val = self.houseRobber3(root.right)
    #         right_pre = self.houseRobber3(root.right.left) + self.houseRobber3(root.right.right)
    #     else:
    #         right_val = right_pre = 0
    #     pre = left_pre + right_pre
    #     curr = left_val + right_val
    #     return max(pre + root.val, curr)


if __name__ == "__main__":
    a = TreeNode(3)
    b = TreeNode(4)
    c = TreeNode(5)
    d = TreeNode(1)
    e = TreeNode(3)
    g = TreeNode(2)
    f = TreeNode(1)
    a.left, a.right = b, c
    b.left, b.right = d, e
    c.right, c.left = f, g
    reslt = Solution().houseRobber3(a)
    print(reslt)