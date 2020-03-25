class Solution:
    """
    @param grids: a integer matrix
    @return: return the difference between two people at last.
    """
    def MatrixGame(self, grids):
        if not grids:
            return 0
        col_max = self.column_max(grids)
        sorted_max = sorted(col_max, reverse=True)
        A = []
        B = []
        turn = 'A'
        for x in sorted_max:
            if turn == 'A':
                A.append(x)
                turn = 'B'
            else:
                B.append(x)
                turn = 'A'
        return sum(A) - sum(B)

    def column_max(self, grids):
        reslt = []
        for i in range(len(grids[0])):
            j = 0
            c_max = grids[j][i]
            while j < len(grids):
                if grids[j][i] > c_max:
                    c_max = grids[j][i]
                j += 1
            reslt.append(c_max)

        return reslt


print(Solution().MatrixGame([[1,4,7],[2,5,8],[3,6,9]]))