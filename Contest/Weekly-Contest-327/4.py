class Solution:
    def findCrossingTime(self, n: int, k: int, time: List[List[int]]) -> int:
        workers = [time[i][0] + time[i][2] for i in range(k)]
        left, right, pick, put = [], [], [], []
        for i, w in enumerate(workers):
            heapq.heappush(left, (-w, -i))

        t = 0
        ans = 0
        while n > 0 or len(right) > 0 or len(pick) > 0 or len(put) > 0:
            if len(right) > 0:
                _, i = heapq.heappop(right)
                i *= -1
                t += time[i][2]
                ans = t
                heapq.heappush(put, (t+time[i][3], i))

            elif n > 0 and len(left) > 0:
                _, i = heapq.heappop(left)
                i *= -1
                t += time[i][0]
                heapq.heappush(pick, (t+time[i][1], i))
                n -= 1

            else:
                tmp = float('inf')
                if put: tmp = min(tmp, put[0][0])
                if pick: tmp = min(tmp, pick[0][0])
                t = tmp

            while put and put[0][0] <= t:
                _, i = heapq.heappop(put)
                heapq.heappush(left, (-workers[i], -i))

            while pick and pick[0][0] <= t:
                _, i = heapq.heappop(pick)
                heapq.heappush(right, (-workers[i], -i))

        return ans
