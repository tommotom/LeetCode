class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)

        xor = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                xor[i][j] = nums1[i] ^ nums2[j]

        dp = {}
        for i in range(n):
            dp[1 << i] = xor[0][i]

        for i in range(1, n):
            tmp = {}
            for old in list(dp.keys()):
                for j in range(n):
                    if not old & (1 << j):
                        new = old | (1 << j)
                        if not new in tmp or tmp[new] > dp[old] + xor[i][j]:
                            tmp[new] = dp[old] + xor[i][j]
            dp = tmp
        return dp[2**n-1]
