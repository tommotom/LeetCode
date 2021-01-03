class Solution:
    def waysToSplit(self, nums: List[int]) -> int:

        modulo = 10 ** 9 + 7

        N = len(nums)
        cum = [nums[0]] + [0 for _ in range(1, N)]
        for i in range(1, N):
            cum[i] = cum[i-1] + nums[i]

        ans = 0
        for i in range(1, N-1):

            left = self.helper(cum, cum[i-1], i, True)
            right = self.helper(cum, cum[i-1], i, False)

            if left == -1 or right == -1: continue

            ans = (ans + (right - left + 1) % modulo) % modulo
        return ans


    def helper(self, cum, leftSum, index, searchLeft):
        N = len(cum)
        l, r = index, N - 2
        res = -1

        while l <= r:
            m = (l + r) // 2
            midSum = cum[m] - cum[index-1]
            rightSum = cum[N - 1] - cum[m]

            if leftSum <= midSum and midSum <= rightSum:
                res = m
                if searchLeft: r = m - 1
                else: l = m + 1
            elif leftSum > midSum: l = m + 1
            else: r = m - 1
        return res
