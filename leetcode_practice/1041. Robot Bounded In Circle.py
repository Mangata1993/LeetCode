class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        direction = ((0, 1), (1, 0), (0, -1), (-1, 0))
        idx = 0
        x, y = 0, 0
        for i in instructions:
            if i == 'L':
                idx = (idx + 1) % 4
            elif i == 'R':
                idx = (idx + 3) % 4
            else:
                x += direction[idx][0]
                y += direction[idx][1]
        return (x == 0 and y == 0) or idx != 0
                
                
