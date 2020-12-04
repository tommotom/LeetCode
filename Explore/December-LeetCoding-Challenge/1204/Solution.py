class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        kth = 0
        for i in range(1, n+1):
            if n % i == 0:
                kth += 1
                if kth == k: return i
        return -1
