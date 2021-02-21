class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        ans = 0
        while Y > X:
            if Y % 2 == 0:
                Y //= 2
            else:
                Y += 1
            ans += 1
        return X - Y + ans
