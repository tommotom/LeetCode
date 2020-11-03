class Solution:
    def maxPower(self, s: str) -> int:
        power, length = 1, len(s)
        last, count = s[0], 1
        for i in range(1, length):
            if s[i] == last:
                count += 1
            else:
                power = max(power, count)
                last, count = s[i], 1

        return max(power, count)
