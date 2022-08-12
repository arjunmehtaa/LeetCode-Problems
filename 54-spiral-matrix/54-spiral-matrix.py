directions = [[0,1], [1,0], [0,-1], [-1,0]]

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        seen = [[False] * len(matrix[0]) for _ in range(len(matrix))]
        size = len(matrix)*len(matrix[0])
        ans = []
        i = 0
        j = 0
        queue = []
        counter = 0
        while True:
            for direction in directions:
                counter += 1
                queue = [[i, j]]
                while len(queue) > 0:
                    element = queue.pop(0)
                    row = element[0]
                    col = element[1]
                    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
                        continue
                    if not seen[row][col]:
                        ans.append(matrix[row][col])
                        if len(ans) == size:
                            return ans
                        seen[row][col] = True
                        i = row
                        j = col
                    queue.append([row + direction[0], col + direction[1]])