class Solution:
    def nextGreaterElement(self, n: int) -> int:
        n_arr = list(str(n))
        n_arr.sort()
        visited = set()
        n_tup = tuple(str(n))
        found = False

        ans = -1

        for v in itertools.permutations(n_arr, len(n_arr)):
            if v in visited: continue
            if found:
                ans = int("".join(v))
                break
            if v == n_tup: found = True
            visited.add(v)

        if ans < 2147483648:
            return ans

        return -1
