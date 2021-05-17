class Solution:
    def sumOfFlooredPairs(self, arr: List[int]) -> int:
        mod = 10 ** 9 + 7
        mx = max(arr)
        counter = Counter(arr)
        cum = [0 for _ in range(2 * mx)]
        for i in range(1, len(cum)):
            cum[i] = cum[i-1]
            if i in counter:
                cum[i] += counter[i]
        ans = 0
        for num in arr:
            l, r, div = num, 2 * num - 1, 1
            while l <= mx:
                ans = (ans + div * (cum[r]-cum[l-1])) % mod
                l += num
                r += num
                div += 1
        return ans
