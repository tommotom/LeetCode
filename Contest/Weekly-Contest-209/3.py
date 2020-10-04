from math import atan2
from math import pi

class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        angles, on = [], 0
        xx, yy = location
        for x, y in points:
            if x == xx and y == yy:
                on += 1
                continue
            angles.append(atan2(y - yy, x - xx))

        angle = angle * pi / 180
        angles.sort()
        angles = angles + [i + 2.0 * pi for i in angles]
        l = ans = 0
        for r in range(len(angles)):
            while angles[r] - angles[l] > angle: l += 1
            ans = max(ans, r - l + 1)

        return ans + on
