class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y, d = 0, 0, "N"

        def step(x, y, d):
            if d == "N":
                return x, y+1
            if d == "E":
                return x+1, y
            if d == "S":
                return x, y-1
            if d == "W":
                return x-1, y

        def turn_left(d):
            if d == "N":
                return "W"
            if d == "E":
                return "N"
            if d == "S":
                return "E"
            if d == "W":
                return "S"

        def turn_right(d):
            if d == "N":
                return "E"
            if d == "E":
                return "S"
            if d == "S":
                return "W"
            if d == "W":
                return "N"

        for i in instructions * 4:
            if i == "G":
                x, y = step(x, y, d)
            elif i == "L":
                d = turn_left(d)
            else:
                d = turn_right(d)

        return x == 0 and y == 0
