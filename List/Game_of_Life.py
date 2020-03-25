class Solution:
    """
    @param board: the given board
    @return: nothing
    """
    def gameOfLife(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                live_count = self.live_count(i, j, board)
                if board[i][j]:
                    if self.live_to_die(live_count):
                        board[i][j] = 'D'
                    if live_count == 2 or live_count == 3:
                        board[i][j] = 1
                if not board[i][j]:
                    if self.die_to_live(live_count):
                        board[i][j] = 'I'
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'D':
                    board[i][j] = 0
                if board[i][j] == 'I':
                    board[i][j] = 1

    def live_to_die(self, live_count):
        return True if live_count < 2 or live_count > 3 else False

    def die_to_live(self, live_count):
        return True if live_count == 3 else False

    def live_count(self, i, j, board):
        live_count = 0
        for k in range(i - 1, i + 2):
            for l in range(j - 1, j + 2):
                if k in range(len(board)) and l in range(len(board[0])):
                    if not (k == i and l == j):
                        live_count += 1 if board[k][l] == 1 or board[k][l] == 'D' else 0
        return live_count


board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Solution().gameOfLife(board)
print(board)