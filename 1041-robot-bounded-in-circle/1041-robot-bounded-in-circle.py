class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dirX = 0
        dirY = 1
        x = 0
        y = 0
        for d in instructions:
            if d == "G":
                x += dirX
                y += dirY            
            elif d == "L":
                dirX, dirY = -dirY, dirX
            else:
                dirX, dirY = dirY, -dirX
        return (x, y) == (0, 0) or (dirX, dirY) != (0, 1)