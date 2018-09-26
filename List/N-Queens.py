class Solution:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """
    def solveNQueens(self, n):
        reslt = []
        chess_board = [["." for i in range(n)] for j in range(n)]
        self.helper(chess_board, 0, reslt, [])
        return reslt

    def helper(self, chess_board, r, reslt, pre):
        if r == len(chess_board):
            reslt.append([''.join(x) for x in chess_board])
            return
        for i in range(len(chess_board)):
            j = 0
            while j < len(pre):
                if pre[j] == i or abs(pre[j] - i) == r - j:
                    break
                j += 1
            if j == len(pre):
                chess_board[r][i] = 'Q'
                pre.append(i)
                self.helper(chess_board, r + 1, reslt, pre)
                chess_board[r][i] = '.'
                pre.pop()


if __name__ == "__main__":
    n = 4
    print(Solution().solveNQueens(n))