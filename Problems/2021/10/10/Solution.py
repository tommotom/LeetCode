class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left == 0: return 0
        ans = 0
        for bit in range(31, -1, -1):
            if (left & (1<<bit)) == (right & (1<<bit)):
                ans += left & (1<<bit)
            else:
                break
        return ans
