from collections import Counter
from collections import defaultdict

class Solution:
    def minDeletions(self, s: str) -> int:
        count = Counter(s)

        dic = defaultdict(lambda: 0)
        for k, v in count.items():
            dic[v] += 1

        n = max(count.values())
        seat = []
        ans = 0
        print(dic)
        for i in range(1, n+1):
            if i not in dic:
                seat.append(i)
                continue
            else:
                while dic[i] > 1:
                    if seat: ans += i - seat.pop()
                    else: ans += i
                    dic[i] -= 1
        return ans
