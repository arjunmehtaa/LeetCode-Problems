# DFS in 2D Array

# Time Complexity   : O(N)
# Space Complexity  : O(N)

def traverseArray(matrix, i, j, seen, ans):
    if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix) or matrix[i][j] in seen:
        return
    ans.append(matrix[i][j])
    seen.add(matrix[i][j])
    traverseArray(matrix, i-1, j, seen, ans)
    traverseArray(matrix, i, j+1, seen, ans)
    traverseArray(matrix, i+1, j, seen, ans)
    traverseArray(matrix, i, j-1, seen, ans)
