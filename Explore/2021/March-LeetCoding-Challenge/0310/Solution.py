class Solution:
    def intToRoman(self, num: int) -> str:
        dic = {4:"IV", 9:"IX", 40:"XL", 90:"XC", 400:"CD", 900:"CM"}
        ans, num = "", str(num)
        for i, c in enumerate(num):
            n = int(c) * 10**(len(num)-i-1)
            if n in dic:
                ans += dic[n]
            else:
                if n >= 1000:
                    while n >= 1000:
                        ans += "M"
                        n -= 1000
                elif n >= 100:
                    if n >= 500:
                        ans += "D"
                        n -= 500
                    while n >= 100:
                        ans += "C"
                        n -= 100
                elif n >= 10:
                    if n >= 50:
                        ans += "L"
                        n -= 50
                    while n >= 10:
                        ans += "X"
                        n -= 10
                elif n >= 1:
                    if n >= 5:
                        ans += "V"
                        n -= 5
                    while n >= 1:
                        ans += "I"
                        n -= 1
        return ans
