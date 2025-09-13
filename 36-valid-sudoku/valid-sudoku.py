class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        box = [set() for _ in range(9)]
        def which_box(i, j):
            if j < 3:
                if i < 3:
                    return 0
                elif i < 6:
                    return 1
                else:
                    return 2
            elif j < 6:
                if i < 3:
                    return 3
                elif i < 6:
                    return 4
                else:
                    return 5
                
            else:
                if i < 3:
                    return 6
                
                elif i < 6:
                    return 7
                
                else:
                    return 8
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    pass
                else:
                    b = which_box(i, j)
                    if board[i][j] in row[i] or board[i][j] in col[j] or board[i][j] in box[b]:
                        return False
                    else:
                        row[i].add(board[i][j])
                        col[j].add(board[i][j])
                        box[b].add(board[i][j])
        return True