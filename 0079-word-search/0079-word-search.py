directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.found = False
        
        def traverse(i, j, index):
            if index == len(word):
                self.found = True
                return
            
            if (i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) 
                or board[i][j] != word[index]):
                return 
            
            savedChar = board[i][j]
            board[i][j] = ""
            for dir in directions:
                traverse(i + dir[0], j + dir[1], index + 1)
            board[i][j] = savedChar
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    traverse(i, j, 0)

        return self.found
                
        
            