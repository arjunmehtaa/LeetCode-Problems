directions = [[-1,0], [1,0], [0,-1], [0,1]]

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        queue = [[sr, sc]]
        start_color = image[sr][sc]
        image[sr][sc] = color
        seen = [[None] * len(image[0]) for k in range(len(image))]
        while len(queue) > 0:
            pos = queue.pop(0)
            row = pos[0]
            col = pos[1]
            for direction in directions:
                next_row = row + direction[0]
                next_col = col + direction[1]
                if next_row < 0 or next_col < 0 or next_row >= len(image) or next_col >= len(image[0]):
                    continue
                if image[next_row][next_col] == start_color:
                    image[next_row][next_col] = color
                    if not seen[next_row][next_col]:
                        queue.append([next_row, next_col])
            seen[row][col] = 1
        return image