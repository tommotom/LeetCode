class Solution:
    def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
        rooms.sort(key=lambda x: x[1], reverse=True)

        queries = [(i, p, m) for i, (p, m) in enumerate(queries)]
        queries.sort(key=lambda x: x[2], reverse=True)

        n, k = len(rooms), len(queries)
        ans = [-1 for _ in range(k)]

        idx = 0
        candidates = []
        for i, p, minSize in queries:
            while idx < n and rooms[idx][1] >= minSize:
                bisect.insort(candidates, rooms[idx][0])
                idx += 1

            if len(candidates) < 1: continue
            if len(candidates) == 1:
                ans[i] = candidates[0]
                continue
            if len(candidates) == 2:
                if abs(candidates[0]-p) <= abs(candidates[1]-p):
                    ans[i] = candidates[0]
                else:
                    ans[i] = candidates[1]
                continue

            l, r = 0, len(candidates) - 1
            m = (l+r) // 2
            left, mid, right = abs(candidates[m-1]-p), abs(candidates[m]-p), abs(candidates[m+1]-p)
            minimum = min(left, mid, right)

            while l + 1 < r:
                m = (l+r) // 2
                left, mid, right = abs(candidates[m-1]-p), abs(candidates[m]-p), abs(candidates[m+1]-p)
                minimum = min(left, mid, right)
                if minimum == left:
                    r = m
                elif minimum == mid:
                    l = r = m
                    break
                else:
                    l = m

            if minimum == left: ans[i]=candidates[l]
            elif minimum == mid: ans[i]=candidates[m]
            else: ans[i]=candidates[r]

        return ans
