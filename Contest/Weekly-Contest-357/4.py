class Solution:
    def findMaximumElegance(self, items: List[List[int]], k: int) -> int:
        items.sort(key=lambda x: x[0], reverse=True)
        ans = cur = 0
        arr = []
        seen = set()
        for i, (p, c) in enumerate(items):
            if i < k:
                if c in seen:
                    arr.append(p)
                cur += p
            elif c not in seen:
                if not arr: break
                cur += p - arr.pop()
            seen.add(c)
            ans = max(ans, cur + len(seen) * len(seen))

        return ans
