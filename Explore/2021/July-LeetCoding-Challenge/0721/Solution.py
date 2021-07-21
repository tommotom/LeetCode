class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        ans = list(dominoes)
        def add(i, d, falling):
            nonlocal ans
            if d == ".":
                return
            elif d == "L":
                if i > 0 and ans[i-1] == ".":
                    if i-1 in falling:
                        del falling[i-1]
                    else:
                        falling[i-1] = d
            else:
                if i+1 < n and ans[i+1] == ".":
                    if i+1 in falling:
                        del falling[i+1]
                    else:
                        falling[i+1] = d

        n = len(dominoes)
        falling = {}

        for i, d in enumerate(dominoes):
            add(i, d, falling)

        while falling:
            tmp = {}
            for i, d in falling.items():
                if ans[i] != ".": continue
                ans[i] = d
                add(i, d, tmp)
            falling = tmp

        return "".join(ans)
