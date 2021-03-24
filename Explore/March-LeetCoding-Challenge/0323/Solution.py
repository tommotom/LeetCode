from collections import Counter

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        counter = Counter(arr)
        ans, modulo = 0, 10 ** 9 + 7
        visited = set()
        for l in counter:
            for m in counter:
                if l == m and counter[l] < 2: continue
                if target - l - m in counter:
                    n = target - l - m

                    a, b, c = sorted([l, m, n])
                    if (a, b, c) in visited: continue
                    visited.add((a, b, c))

                    if a == b == c:
                        if counter[a] < 3: continue
                        ans += counter[a] * (counter[a] - 1) * (counter[a] - 2) // 6
                    elif a == b or b == c:
                        if counter[b] < 2: continue
                        ans += counter[a] * (counter[b] - 1) * counter[c] // 2
                    else:
                        ans += counter[a] * counter[b] * counter[c]
                    ans %= modulo

        return ans
