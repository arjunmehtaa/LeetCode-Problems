class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        for i in range(len(matrix)):
            for j in range(i, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
        for row in matrix:
            row.reverse()
        
        # stack = []
        # for j in range(0, len(matrix[0])):
        #     for i in range(len(matrix) - 1, -1, -1):
        #         stack.append(matrix[i][j])
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         matrix[i][j] = stack.pop(0)
            