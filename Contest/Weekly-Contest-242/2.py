class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if len(dist)-1 > hour: return -1
        l, r = 1, 10**9
        while l < r:
            speed = (l+r) // 2
            took = 0
            for d in dist[:-1]:
                took += math.ceil(d/speed)
                if took > hour:
                    l = speed + 1
                    break
            else:
                if took + dist[-1]/speed <= hour:
                    r = speed
                else:
                    l = speed + 1
        return l
