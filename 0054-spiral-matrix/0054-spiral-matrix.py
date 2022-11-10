class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        totalRows = len(matrix)
        totalCols = len(matrix[0])
        total = totalRows * totalCols
        ans = []
        
        top = 0
        bottom = totalRows - 1
        left = 0
        right = totalCols - 1
        
        while len(ans) < total:
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
            
        return ans[:total]
        