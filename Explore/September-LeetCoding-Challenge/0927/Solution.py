from collections import defaultdict
from collections import deque

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        nums = defaultdict(list)
        for i in range(len(equations)):
            a, b = equations[i][0], equations[i][1]
            nums[a].append((values[i], b))
            nums[b].append((1/values[i], a))

        ans = []
        for query in queries:
            a, b = query[0], query[1]
            visited = set()
            q = deque([(1.0, a)])
            while q:
                val, now = q.popleft()
                if now not in nums: continue
                if now == b:
                    ans.append(val)
                    break
                visited.add(now)
                for mul, dist in nums[now]:
                    if dist in visited: continue
                    q.append((val * mul, dist))
            else:
                ans.append(-1.0)

        return ans
