class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:

        def ope(cur, num):
            return [cur+num, cur-num, cur^num]

        q = deque([(start, 0)])
        visited = set()
        while q:
            cur, step = q.popleft()
            for num in nums:
                candidates = ope(cur, num)
                for c in candidates:
                    if c in visited:
                        continue
                    if c == goal:
                        return step+1
                    if not 0 <= c <= 1000: continue
                    visited.add(c)
                    q.append((c, step+1))
        return -1
