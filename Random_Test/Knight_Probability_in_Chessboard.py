import decimal


class Solution:
    """
    @param N: int
    @param K: int
    @param r: int
    @param c: int
    @return: the probability
    """
    def knightProbability(self, N, K, r, c):
        dp = [[1 for i in range(N)] for j in range(N)]
        possible_move = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
        move_table = [[[] for i in range(N)] for j in range(N)]
        for move in range(0, K):
            temp = [[0 for i in range(N)] for j in range(N)]
            for i in range(N):
                for j in range(N):
                    if move == 0:
                        for x in possible_move:
                            if (i + x[0] in range(0, N)) and (j + x[1] in range(0, N)):
                                move_table[i][j].append(x)
                                temp[i][j] += dp[i + x[0]][j + x[1]]
                    else:
                        for x in move_table[i][j]:
                            temp[i][j] += dp[i + x[0]][j + x[1]]
            dp = temp

        context = decimal.getcontext()
        context.rounding = decimal.ROUND_HALF_UP
        return round(dp[r][c] / 8**K, 2)


print(Solution().knightProbability(25,32,15,8))
