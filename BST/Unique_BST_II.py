class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    # @paramn n: An integer
    # @return: A list of root
    def generateTrees(self, n):
        memo = [[None], [TreeNode(1)]]
        return self.dfs(1, n, memo)

    def dfs(self, start, end, memo):
        if start > end:
            return [None]
        reslt = []
        for rootVal in range(start, end + 1):
            if start == 1:
                left = memo[rootVal - 1]
            else:
                left = self.dfs(start, rootVal - 1, memo)
            right = self.dfs(rootVal + 1, end, memo)
            for i in left:
                for j in right:
                    root = TreeNode(rootVal)
                    root.left = i
                    root.right = j
                    reslt.append(root)
        memo.append(reslt)
        return reslt


if __name__ == "__main__":
    n = 3
    reslt = Solution().generateTrees(n)
    print(reslt)