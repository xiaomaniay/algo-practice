class Solution:
    """
    @param n: The number of queens.
    @return: The total number of distinct solutions.
    """
    def totalNQueens(self, n):
        chess_board = [["." for i in range(n)] for j in range(n)]
        return self.helper(chess_board, 0, [])

    def helper(self, chess_board, r, pre):
        reslt = 0
        if r == len(chess_board):
            return reslt + 1
        for i in range(len(chess_board)):
            j = 0
            while j < len(pre):
                if pre[j] == i or abs(pre[j] - i) == r - j:
                    break
                j += 1
            if j == len(pre):
                chess_board[r][i] = 'Q'
                pre.append(i)
                reslt += self.helper(chess_board, r + 1, pre)
                chess_board[r][i] = '.'
                pre.pop()
        return reslt


if __name__ == "__main__":
    n = 4
    print(Solution().totalNQueens(n))

