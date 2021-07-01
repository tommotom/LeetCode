class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        mod = 10 ** 9 + 7
        dp = [1 for _ in range(len(arr))]
        index = {x:i for i, x in enumerate(arr)}
        for i, x in enumerate(arr):
            for j in range(i):
                if x % arr[j] == 0:
                    tmp = x // arr[j]
                    if tmp in index:
                        dp[i] += dp[j] * dp[index[tmp]]
                        dp[i] %= mod
        return sum(dp) % mod
