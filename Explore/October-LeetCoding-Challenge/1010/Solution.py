class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points: return 0
        points = sorted(points, key=lambda x: (x[0], -x[1]))
        ans, end = 1, points[0][1]
        for i in range(1, len(points)):
            if points[i][0] <= end:
                end = min(end, points[i][1])
            else:
                ans += 1
                end = points[i][1]
        return ans
