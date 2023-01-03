class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        ans = 1
        num = 0
        for c in s:
            num *= 10
            num += int(c)
            if num > k:
                ans += 1
                num %= 10
            if num > k: return -1
        return ans
