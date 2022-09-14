class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        total = rows * cols
        answer = []
        top, bottom = 0, rows - 1
        left, right = 0, cols - 1
        while len(answer) < total:
            for i in range(left, right + 1):
                answer.append(matrix[top][i])
            top += 1
            for i in range(top, bottom + 1):
                answer.append(matrix[i][right])
            right -= 1
            for i in range(right, left - 1, -1):
                answer.append(matrix[bottom][i])
            bottom -= 1
            for i in range(bottom, top - 1, -1):
                answer.append(matrix[i][left])
            left += 1
        return answer[:total]
                