class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        memo = {}
        memo[0], memo[1] = False, True
        def helper(num):
            nonlocal memo
            if num in memo: return memo[num]
            for j in range(1, int(num**0.5)+1):
                if not helper(num-j**2):
                    memo[num] = True
                    return True
            memo[num] = False
            return False

        return helper(n)
