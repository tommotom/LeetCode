class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        q = []
        for k, v in Counter(s).items():
            heapq.heappush(q, (-ord(k), k, v))

        arr = []
        def helper(k, v, limit):
            count = min(limit, v)
            for __ in range(count):
                arr.append(k)
            v -= count
            if v > 0:
                heapq.heappush(q, (-ord(k), k, v))

        while q:
            _, k, v = heapq.heappop(q)
            if not arr or arr[-1] != k:
                helper(k, v, repeatLimit)
                continue

            if not q: break

            __, k2, v2 = heapq.heappop(q)
            helper(k2, v2, 1)
            heapq.heappush(q, (-ord(k), k, v))

        return "".join(arr)
