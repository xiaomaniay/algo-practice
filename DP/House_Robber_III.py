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
        memo = {None: 0}

        def dfs(root):
            if root not in memo.keys():
                left, right = root.left, root.right
                ll = lr = rl = rr = None
                if root.left:
                    ll, lr = left.left, left.right
                if root.right:
                    rl, rr = right.left, right.right
                pre = dfs(ll) + dfs(lr) + dfs(rl) + dfs(rr)
                curr = dfs(left) + dfs(right)
                memo[root] = max(pre + root.val, curr)
            return memo[root]
        return dfs(root)

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