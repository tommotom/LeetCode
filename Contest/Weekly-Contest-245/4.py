class Solution:
    def earliestAndLatest(self, n: int, f: int, s: int) -> List[int]:
        ans = set()
        def dfs(pos, i):
            M, pairs = len(pos), []
            if M < 2: return

            for j in range(M//2):
                a, b = pos[j], pos[-1-j]
                if (a, b) == (f, s):
                    ans.add(i)
                    return
                if a != f and b != f and a != s and b != s:
                    pairs.append((a, b))
            addon = (f, s) if M % 2 == 0 else tuple(set([f, s, pos[M//2]]))
            for elem in product(*pairs):
                dfs(sorted(elem + addon), i+1)

        dfs(list(range(1, n+1)), 1)
        return [min(ans), max(ans)]
