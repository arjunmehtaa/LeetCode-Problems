directions = [[-1,0], [1,0], [0,-1], [0,1]]

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start_color = image[sr][sc]
        if start_color == color:
            return image
        queue = [[sr, sc]]
        image[sr][sc] = color
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
                    queue.append([next_row, next_col])
        return image