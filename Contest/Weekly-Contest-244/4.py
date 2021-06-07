class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        n, m = len(packages), len(boxes)
        packages.sort()
        cum = [0 for _ in range(n)]
        cum[0] = packages[0]
        for i in range(1, n):
            cum[i] = cum[i-1] + packages[i]

        ans = float("inf")
        for i in range(m):
            box = sorted(boxes[i])
            if packages[-1] > box[-1]: continue
            tmp = 0
            placed = -1
            for j in range(len(box)):
                idx = bisect.bisect(packages, box[j]) - 1
                if idx == placed: continue
                tmp += box[j]*(idx - placed) - (cum[idx] - (cum[placed] if placed >= 0 else 0))
                placed = idx
                if placed == len(packages): break
            ans = min(ans, tmp)

        return -1 if ans == float("inf") else ans % (10**9+7)
