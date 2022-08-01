class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        boxes = [dict() for _ in range(n)]
        rows = [dict() for _ in range(n)]
        cols = [dict() for _ in range(n)]
        for r in range(0, n):
            for c in range(0, n):
                if board[r][c] != ".":
                    val = board[r][c]
                    box_id = getBoxId(r, c)
                    boxes[box_id][val] = True
                    rows[r][val] = True
                    cols[c][val] = True
        solveBacktrack(board, boxes, rows, cols, 0, 0)
        
def getBoxId(row, col):
    col_val = floor(col/3)
    row_val = floor(row/3) * 3
    return row_val + col_val
        
def isValid(box, row, col, num):
    if (num in box) or (num in row) or (num in col):
        return False
    return True    
                
def solveBacktrack(board, boxes, rows, cols, r, c):
    if r == len(board) or c == len(board[0]):
        return True
    if board[r][c] == ".":
        for num in range(1, 9+1):
            num_val = str(num)
            board[r][c] = num_val
            box_id = getBoxId(r, c)
            box = boxes[box_id]
            row = rows[r]
            col = cols[c]
            if isValid(box, row, col, num_val):
                box[num_val] = True   
                row[num_val] = True 
                col[num_val] = True 
                if c == len(board[0]) - 1:
                    if solveBacktrack(board, boxes, rows, cols, r+1, 0):
                        return True
                else:
                    if solveBacktrack(board, boxes, rows, cols, r, c+1):
                        return True
                del box[num_val]  
                del row[num_val]
                del col[num_val]
            board[r][c] = "."
    else:
        if c == len(board[0]) - 1:
            if solveBacktrack(board, boxes, rows, cols, r+1, 0):
                return True
        else:
            if solveBacktrack(board, boxes, rows, cols, r, c+1):
                return True
    return False