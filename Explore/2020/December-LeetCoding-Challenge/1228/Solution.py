class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        position = step = 0

        while position < target:
            step += 1
            position += step

        while True:
            if (target - position) % 2 == 0: return step
            step += 1
            position += step

