directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        numRows = len(board)
        numCols = len(board[0])
        
        def traverse(i, j, index):
            if index >= len(word):
                return True
            if i < 0 or j < 0 or i >= numRows or j >= numCols:
                return False
            if board[i][j] == word[index]:
                temp = board[i][j]
                board[i][j] = ""
                for direction in directions:
                    nextRow = i + direction[0]
                    nextCol = j + direction[1]
                    if traverse(nextRow, nextCol, index + 1):
                        return True
                board[i][j] = temp
            return False
        
        for i in range(numRows):
            for j in range(numCols):
                if traverse(i, j, 0):
                    return True
                
        return False
        
        
            