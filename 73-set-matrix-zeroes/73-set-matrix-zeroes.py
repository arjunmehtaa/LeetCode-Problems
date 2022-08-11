directions = [[-1,0], [0,-1], [0,1], [1,0]]

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ignore = []
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if matrix[i][j] == 0 and [i,j] not in ignore:
                    traverse(i, j, matrix, ignore)
                        
def traverse(i, j, matrix, ignore):
    for direction in directions:
        row = i + direction[0]
        col = j + direction[1]
        queue = [[row, col]]
        while len(queue) > 0:
            element = queue.pop(0)
            next_row = element[0]
            next_col = element[1]
            if next_row < 0 or next_col < 0 or next_row >= len(matrix) or next_col >= len(matrix[0]):
                continue
            if matrix[next_row][next_col] != 0:
                matrix[next_row][next_col] = 0
                ignore.append([next_row, next_col])
            queue.append([next_row + direction[0], next_col + direction[1]])
        