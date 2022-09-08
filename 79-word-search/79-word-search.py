directions = [[-1,0], [1,0], [0,-1], [0,1]]

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        path = set()
        
        def dfs(r, c, i):
            if i == len(word):
                return True
            if r < 0 or c < 0 or r >= rows or c >= cols or word[i] != board[r][c] or (r, c) in path:
                return False
            path.add((r, c))
            for direction in directions:
                next_row = r + direction[0]
                next_col = c + direction[1]
                if dfs(next_row, next_col, i + 1):
                    return True
            path.remove((r, c))
            return False
            
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
                
        return False