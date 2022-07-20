class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        ans = [[None]*len(matrix) for k in range(0, len(matrix[0]))]
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
               ans[j][i] = matrix[i][j]
        return ans 
    
        # ans = []
        # for j in range(0, len(matrix[0])):
        #     column = []
        #     for i in range(0, len(matrix)):
        #         column.append(matrix[i][j])
        #     ans.append(column)
        # return ans