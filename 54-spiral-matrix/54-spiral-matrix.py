directions = [[0,1], [1,0], [0,-1], [-1,0]]

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        total = len(matrix)*len(matrix[0]) - 1
        ans = [matrix[0][0]]
        row, col = 0, 0
        seen = set()
        seen.add((0, 0))
        while total > 0:
            for direction in directions:
                row += direction[0]
                col += direction[1]
                while (row >= 0 
                       and col >= 0 
                       and row < len(matrix) 
                       and col < len(matrix[0]) 
                       and (row, col) not in seen):
                    ans.append(matrix[row][col])
                    total -= 1
                    seen.add((row, col))
                    row += direction[0]
                    col += direction[1]
                row -= direction[0]
                col -= direction[1]
        return ans
                    