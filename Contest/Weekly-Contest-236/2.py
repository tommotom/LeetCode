class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        org = n
        dead = [False for _ in range(n)]
        idx = 0
        while n > 1:
            tmp = k-1
            while tmp > 0:
                if not dead[idx]:
                    tmp -= 1
                idx = (idx + 1) % org
            while dead[idx]:
                idx = (idx + 1) % org
            dead[idx] = True
            n -= 1

        for i, d in enumerate(dead):
            if not d: return i+1
