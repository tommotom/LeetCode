class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        num = -float('inf')
        ans = ""
        for i in range(len(number)):
            if number[i] == digit and int(number[:i] + number[i+1:]) > num:
                ans = number[:i] + number[i+1:]
                num = int(ans)
        return ans
