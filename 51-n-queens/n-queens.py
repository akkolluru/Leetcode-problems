class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        answer = []
        board = [["."] * n for _ in range(n)]
        def nqueens(row, cols, diag1, diag2, board):
            if row == n:
                answer.append(["".join(r) for r in board])
                return
            for col in range(n):
                if col in cols or row - col in diag1 or row + col in diag2:
                    continue
                else:
                    board[row][col] = "Q"
                    cols.add(col)
                    diag1.add(row - col)
                    diag2.add(row + col)
                    nqueens(row+1, cols, diag1, diag2, board)


                    board[row][col] = "."
                    cols.remove(col)
                    diag1.remove(row - col)
                    diag2.remove(row + col)
        nqueens(0, set(), set(), set(), board)
        return answer