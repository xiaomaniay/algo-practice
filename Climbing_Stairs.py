class Solution:
    """
    @param n: An integer
    @return: An integer
    """

    def climbStairs(self, n):
        if n == 0:
            return 0
        memo = [1, 1]
        for i in range(2, n + 1):
            temp = memo[1]
            memo[1] += memo[0]
            memo[0] = temp

        return memo[1]