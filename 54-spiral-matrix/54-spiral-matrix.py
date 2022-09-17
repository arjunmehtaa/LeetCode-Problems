class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        rows, cols = len(matrix), len(matrix[0])
        total = rows * cols
        top, bottom = 0, rows - 1
        left, right = 0, cols - 1
        while len(res) < total:
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1
            for i in range(right, left - 1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
        return res[:total]
        
        