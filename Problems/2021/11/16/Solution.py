class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        if n > m: n, m = m, n

        l, r = 1, m*n

        while l <= r:
            target = (l+r) // 2

            th_min = 1
            th_max = 0
            include_myself = False
            for row in range(m):
                th_min += min(target // (row+1) - (1 if target % (row+1) == 0 else 0), n)
                th_max += min(target // (row+1), n)
                if min(target // (row+1), n) * (row + 1) == target: include_myself = True

            if not include_myself: th_max += 1

            if th_min <= k <= th_max:
                while not any(min(target // (row+1), n) * (row+1) == target for row in range(m)): target += 1
                return target
            elif k > th_max:
                l = target + 1
            else:
                r = target - 1
