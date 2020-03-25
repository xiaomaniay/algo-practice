class Solution:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """
    def solveNQueens(self, n):
        reslt = []
        chess_board = [["." for i in range(n)] for j in range(n)]  # initialize the chessboard
        self.helper(chess_board, 0, reslt, [])
        return reslt

    def helper(self, chess_board, r, reslt, pre):
        if r == len(chess_board):  # queen is placed at last row, one solution generated
            reslt.append([''.join(x) for x in chess_board])  # add the solution to results list
            return
        for i in range(len(chess_board)):  # for each column in chessboard
            j = 0  # start from the first column
            while j < len(pre):  # check each of the previous occupied position
                if pre[j] == i or abs(pre[j] - i) == r - j:  # if on the same column or on the same diagonal
                    break  # no queen should placed at the position, proceed to next i
                j += 1  # proceed to the next position
            if j == len(pre):  # all previous positions checked
                chess_board[r][i] = 'Q'  # place a Q at position [r][i]
                pre.append(i)  # record the occupied position in pre
                self.helper(chess_board, r + 1, reslt, pre)  # proceed to next row
                chess_board[r][i] = '.'  # revert Q to . and try next possible solution
                pre.pop()  # [r][i] does not work, proceed to [r][i + 1]


if __name__ == "__main__":
    n = 4
    print(Solution().solveNQueens(n))