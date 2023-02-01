directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        
        def dfs(index, r, c):
            if index >= len(word):
                return True
            if r < 0 or c < 0 or r >= n or c >= m or board[r][c] != word[index]:
                return False
            char = board[r][c]
            board[r][c] = ""
            ans = False
            for d in directions:
                if dfs(index + 1, r + d[0], c + d[1]):
                    ans = True
                    break
            board[r][c] = char
            return ans
        
        for i in range(n):
            for j in range(m):
                if dfs(0, i, j):
                    return True
        
        return False