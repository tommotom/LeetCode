from collections import defaultdict

class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        n = len(A)
        AB = defaultdict(lambda: 0)
        CD = defaultdict(lambda: 0)

        for i in range(n):
            for j in range(n):
                tmp = A[i] + B[j]
                AB[tmp] += 1

        for i in range(n):
            for j in range(n):
                tmp = C[i] + D[j]
                CD[tmp] += 1

        ans = 0
        for k, v in AB.items():
            ans += CD[-k] * v

        return ans