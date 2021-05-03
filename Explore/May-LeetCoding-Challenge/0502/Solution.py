class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x:x[1])
        now = 0
        took = []
        for time, until in courses:
            if now + time <= until:
                heapq.heappush(took, -time)
                now += time
            else:
                if took and -took[0] > time and now + took[0] + time < until:
                    now += heapq.heappop(took)
                    heapq.heappush(took, -time)
                    now += time
        return len(took)
