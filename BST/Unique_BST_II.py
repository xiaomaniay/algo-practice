class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    # @paramn n: An integer
    # @return: A list of root
    def generateTrees(self, n):
        return self.dfs(1, n,)

    def dfs(self, start, end):
        if start > end:
            return [None]
        reslt = []
        for rootVal in range(start, end + 1):
            left = self.dfs(start, rootVal - 1)
            right = self.dfs(rootVal + 1, end)
            for i in left:
                for j in right:
                    root = TreeNode(rootVal)
                    root.left = i
                    root.right = j
                    reslt.append(root)
        return reslt


if __name__ == "__main__":
    n = 3
    reslt = Solution().generateTrees(n)
    print(reslt)