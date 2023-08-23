class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        q = []
        for k, v in counter.items():
            heapq.heappush(q, (-v, k))
        arr = []
        while q:
            v, k = heapq.heappop(q)
            if arr and arr[-1] == k:
                if not q: return ""
                v2, k2 = heapq.heappop(q)
                arr.append(k2)
                if v2 < -1:
                    heapq.heappush(q, (v2+1, k2))
            else:
                arr.append(k)
                v += 1
            if v < 0:
                heapq.heappush(q, (v, k))

        return "".join(arr)
