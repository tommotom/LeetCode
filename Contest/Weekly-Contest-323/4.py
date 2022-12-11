class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        q = [(grid[0][0], 0, 0)]
        cur = grid[0][0]
        score = 0
        visited = set([(0,0)])
        directions = ((0,1),(0,-1),(1,0),(-1,0))
        vals = []
        scores = []
        while q:
            val, r, c = heapq.heappop(q)
            if val > cur:
                vals.append(cur)
                scores.append(score)
                cur = val
                score = 1
            else:
                score += 1
            for d in directions:
                n_r = r + d[0]
                if n_r < 0 or n_r >= len(grid): continue
                n_c = c + d[1]
                if n_c < 0 or n_c >= len(grid[0]): continue
                key = (n_r, n_c)
                if key in visited: continue
                visited.add(key)
                heapq.heappush(q, (grid[n_r][n_c], n_r, n_c))
        vals.append(cur)
        scores.append(score)
        scores = list(itertools.accumulate(scores))
        ans = []
        for query in queries:
            if query <= grid[0][0]:
                ans.append(0)
                continue
            i = bisect.bisect_left(vals, query)
            ans.append(scores[i-1])

        return ans
