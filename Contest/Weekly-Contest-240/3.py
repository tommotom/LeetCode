class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        n, ans, mod = len(nums), 0, 10 ** 9 + 7

        l, st = [0], [[nums[0], 0]]
        for i in range(1, n):
            cur = 0
            while st and nums[i] <= st[-1][0]:
                cur += st.pop()[1] + 1
            st.append([nums[i], cur])
            l.append(cur)

        r, st = [0], [[nums[-1], 0]]
        for i in range(n-2, -1, -1):
            cur = 0
            while st and st[-1][0] >= nums[i]:
                cur += st.pop()[1] + 1
            st.append([nums[i], cur])
            r.append(cur)
        r.reverse()

        sums, cur = [0], 0
        for i in range(n):
            cur += nums[i]
            sums.append(cur)

        for i in range(n):
            ans = max(ans, nums[i] * (sums[i + r[i] + 1] - sums[i - l[i]]))

        return ans % mod
