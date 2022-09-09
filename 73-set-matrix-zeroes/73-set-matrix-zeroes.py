directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        totalRows = len(matrix)
        totalCols = len(matrix[0])
        queue = []
        
        for i in range(totalRows):
            for j in range(totalCols):
                if matrix[i][j] == 0:
                    queue.append([i, j])
                    
        while len(queue) > 0:
            element = queue.pop(0)
            r, c = element[0], element[1]
            for direction in directions:
                nextRow = r + direction[0]
                nextCol = c + direction[1]
                while nextRow >= 0 and nextCol >= 0 and nextRow < totalRows and nextCol < totalCols:
                    matrix[nextRow][nextCol] = 0
                    nextRow += direction[0]
                    nextCol += direction[1]
        
        return matrix