class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digits = len(str(low))
        first = int(str(low)[0])
        ans = []
        while True:
            if digits + first > 10:
                first = 1
                digits += 1

            num = 0
            for i in range(digits):
                num += (first + i) * 10 ** (digits - 1 - i)

            if num > high: break

            if num >= low:
                ans.append(num)
            if first < 9:
                first += 1
            else:
                first = 1
                digits += 1

        return ans
