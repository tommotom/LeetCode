class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def inc(num):
            if num == 9:
                return 0
            return num + 1
        def dec(num):
            if num == 0:
                return 9
            return num -1

        visited = set()
        for d in deadends:
            visited.add(tuple(map(int, list(d))))
        q = collections.deque([(0,0,0,0,0)])
        target = tuple(map(int,target))
        while q:
            turn, a, b, c, d = q.popleft()
            if (a, b, c, d) == target:
                return turn
            if (a, b, c, d) in visited:
                continue
            visited.add((a, b, c, d))
            if (inc(a), b, c, d) not in visited:
                q.append((turn+1, inc(a), b, c, d))
            if (dec(a), b, c, d) not in visited:
                q.append((turn+1, dec(a), b, c, d))
            if (a, inc(b), c, d) not in visited:
                q.append((turn+1, a, inc(b), c, d))
            if (a, dec(b), c, d) not in visited:
                q.append((turn+1, a, dec(b), c, d))
            if (a, b, inc(c), d) not in visited:
                q.append((turn+1, a, b, inc(c), d))
            if (a, b, dec(c), d) not in visited:
                q.append((turn+1, a, b, dec(c), d))
            if (a, b, c, inc(d)) not in visited:
                q.append((turn+1, a, b, c, inc(d)))
            if (a, b, c, dec(d)) not in visited:
                q.append((turn+1, a, b, c, dec(d)))

        return -1
