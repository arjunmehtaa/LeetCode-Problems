directions = [[-1,-1], [-1, 0], [-1,1], [0,-1], [0,1], [1,-1], [1,0], [1,1]]

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        result = [[None] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                count = 0 
                for direction in directions:
                    r = i + direction[0]
                    c = j + direction[1]
                    if r < 0 or c < 0 or r >= rows or c >= cols:
                        continue
                    if board[r][c] == 1 or board[r][c] == 3:
                        count += 1
                if board[i][j] == 1 or board[i][j] == 3:
                    if count == 2 or count == 3:
                        board[i][j] = 1
                    else:
                        board[i][j] = 3
                if board[i][j] == 0 or board[i][j] == 2:
                    if count == 3:
                        board[i][j] = 2
                    else:
                        board[i][j] = 0
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] == 3:
                    board[i][j] = 0

        # 0 0 -> 0
        # 1 1 -> 1
        # 0 1 -> 2
        # 1 0 -> 3
                        