class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:(x[0], x[1]))
        i = j = ans = 0
        while i < len(points):
            end = points[i][1]
            while j+1 < len(points) and points[j+1][0] <= end:
                j += 1
                end = min(end, points[j][1])
            ans += 1
            i = j+1
        return ans
