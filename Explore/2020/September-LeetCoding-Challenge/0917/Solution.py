class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        position, direction = self.compression(instructions)
        x, y = position
        if x == 0 and y == 0: return True
        if direction == 90: return False
        return True


    def compression(self, instructions):
        position = [0, 0]
        direction = 90
        for i in instructions:
            if i == 'G': position = self.move(position, direction)
            else: direction = self.rotate(direction, i)
        return position, direction

    def move(self, position, direction):
        if direction == 90: position[1] += 1
        elif direction == 270: position[1] -= 1
        elif direction == 0: position[0] += 1
        elif direction == 180: position[0] -= 1
        return position

    def rotate(self, direction, to):
        if to == 'L': return (direction + 90) % 360
        else: return (direction + 270) % 360
