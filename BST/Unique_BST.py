class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def numTrees(self, n):
        # memo = {0: 1, 1: 1}
        # mid = int((n + 1) / 2)
        # if n > 1:
        #     memo[n] = 0
        #     for i in range(1, mid + 1):
        #         if (i - 1) in memo.keys():
        #             leftNum = memo[i - 1]
        #         else:
        #             leftNum = self.numTrees(i - 1)
        #         if (n - i) in memo.keys():
        #             rightNum = memo[n - i]
        #         else:
        #             rightNum = self.numTrees(n - i)
        #         memo[n] = memo[n] + (2 if i <= (n / 2) else 1) * leftNum * rightNum
        # return memo[n]
        memo = [1, 1]
        if n > 1:
            memo += [0 for i in range(n - 1)]
            for i in range(2, n + 1):
                for j in range(1, i + 1):
                    memo[i] += memo[j - 1] * memo[i - j]
        return memo[n]


if __name__ == "__main__":
    n = 15
    reslt = Solution().numTrees(n)
    print(reslt)