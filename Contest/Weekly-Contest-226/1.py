from collections import defaultdict

class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        dic = defaultdict(lambda:0)
        for i in range(lowLimit, highLimit+1):
            tmp = 0
            while i > 0:
                tmp += i % 10
                i //= 10
            dic[tmp] += 1
        return max(dic.values())
