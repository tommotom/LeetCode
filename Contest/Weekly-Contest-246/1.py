class Solution:
    def largestOddNumber(self, num: str) -> str:
        ans = ""
        for i, n in enumerate(num):
            if int(n) % 2 == 1:
                ans = max(ans, num[:i+1])
        return ans
