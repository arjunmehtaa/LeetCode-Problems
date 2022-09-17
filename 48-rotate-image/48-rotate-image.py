class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows):
            for j in range(i, cols):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
        for row in matrix:
            row.reverse()
            
        