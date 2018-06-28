class Solution:
    """
    @param n: an integer
    @return: an ineger f(n)
    """
    memo = {1: 0, 2: 1}

    def fibonacci(self, n):

        if n in Solution.memo:
            return Solution.memo[n]
        else:
            res = self.fibonacci(n-1) + self.fibonacci(n-2)
            Solution.memo[n] = res
            return Solution.memo[n]