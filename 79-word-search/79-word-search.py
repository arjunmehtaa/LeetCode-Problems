directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        self.found = False
        
        def backtrack(i, j, index):
            if index >= len(word):
                self.found = True
                return
            if i < 0 or j < 0 or i >= rows or j >= cols or board[i][j] != word[index]:
                return
            char = board[i][j]
            board[i][j] = ""
            for direction in directions:
                backtrack(i + direction[0], j + direction[1], index + 1)  
            board[i][j] = char
            
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    backtrack(i, j, 0)
            
        return self.found