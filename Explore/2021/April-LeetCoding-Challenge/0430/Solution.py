class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        xi, yj = set([1]), set([1])

        if x != 1:
            tmp = 1
            while tmp < bound:
                xi.add(tmp)
                tmp *= x

        if y != 1:
            tmp = 1
            while tmp < bound:
                yj.add(tmp)
                tmp *= y

        ans = set()
        for a in xi:
            for b in yj:
                if a + b > bound: continue
                ans.add(a+b)

        return list(ans)
