# rationale: no two queens can share the same row
# complexity: n**n


class Solution:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """
    def solveNQueens(self, n):
        chessboard = [["." for i in range(n)] for j in range(n)]
        reslts = []
        self.place_queen(chessboard, 0, [], reslts)
        return reslts

    def place_queen(self, chessboard, r, pre, reslts):
        if r == len(chessboard):  # all n queens placed
            reslts.append([''.join(x) for x in chessboard])
            return
        for i in range(len(chessboard)):
            if self.valid_position(r, i, pre):
                chessboard[r][i] = 'Q'
                pre.append(i)
                self.place_queen(chessboard, r + 1, pre, reslts)
                chessboard[r][i] = '.'
                pre.pop()

    def valid_position(self, r, c, pre):
        for j in range(len(pre)):
            if pre[j] == c or abs(c - pre[j]) == r - j:
                return False
            j += 1
        return True


if __name__ == "__main__":
    n = 5
    print(Solution().solveNQueens(n))