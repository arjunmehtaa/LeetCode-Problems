# BFS in 2D Array

# Time Complexity   : O(N)
# Space Complexity  : O(N)

# Note: If values are allowed to be duplicate, seen functionality would have to change
# to a an array of boolean values, where we can check if seen[i][j] is true

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        seen = set()
        ans = []
        queue = [[0,0]]
        while len(queue) > 0:
            position = queue.pop(0)
            i = position[0]
            j = position[1]
            if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]) or matrix[i][j] in seen:
                continue
            ans.append(matrix[i][j])
            seen.add(matrix[i][j])
            queue.append([i-1, j])
            queue.append([i, j+1])
            queue.append([i+1, j])
            queue.append([i, j-1])
        print(ans)
        
