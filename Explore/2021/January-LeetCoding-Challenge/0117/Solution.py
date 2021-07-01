class Solution:
    def countVowelStrings(self, n: int) -> int:
        memo = {}

        def dfs(length, cur):
            nonlocal memo

            if (length, cur) in memo:
                return memo[(length, cur)]

            if length == n:
                memo[(length, cur)] = 1
                return memo[(length, cur)]

            tmp = 0
            for i in range(cur, 5):
                tmp += dfs(length + 1, i)

            memo[(length, cur)] = tmp

            return memo[(length, cur)]

        return dfs(0, 0)
