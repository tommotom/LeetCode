import math

class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        def combinations_count(v, h):
            return math.factorial(v+h) // (math.factorial(v) * math.factorial(h))

        ans = ""
        def helper(v, h, count):
            nonlocal k, ans
            if v == h == 0: return
            if v == 0:
                ans += "H" * h
                return
            if h == 0:
                ans += "V" * v
                return

            comb = combinations_count(v, h-1)
            if k <= count + comb:
                ans += "H"
                helper(v, h-1, count)
            else:
                ans += "V"
                helper(v-1, h, count+comb)

        helper(destination[0], destination[1], 0)
        return ans
