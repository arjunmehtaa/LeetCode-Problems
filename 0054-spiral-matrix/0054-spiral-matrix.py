class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        numRows = len(matrix)
        numCols = len(matrix[0])
        totalElements = numRows * numCols
        top, bottom = 0, numRows - 1
        left, right = 0, numCols - 1
        while len(ans) < totalElements:
            for i in range(left, right + 1):
                ans.append(matrix[top][i])
            top += 1
            for i in range(top, bottom + 1):
                ans.append(matrix[i][right])
            right -= 1
            for i in range(right, left - 1, -1):
                ans.append(matrix[bottom][i])
            bottom -= 1
            for i in range(bottom, top - 1, -1):
                ans.append(matrix[i][left])
            left += 1
        return ans[:totalElements]