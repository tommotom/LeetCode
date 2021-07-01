class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visited = set()
        rows, cols = len(grid), len(grid[0])
        heap = [(grid[0][0], 0, 0)]
        ans = 0
        while True:
            ele, r, c = heapq.heappop(heap)
            visited.add((r, c))
            ans = max(ans, ele)
            if r == rows-1 and c == cols-1:
                return ans
            if r > 0 and (r-1, c) not in visited:
                visited.add((r-1, c))
                heapq.heappush(heap, (grid[r-1][c], r-1, c))
            if c > 0 and (r, c-1) not in visited:
                visited.add((r, c-1))
                heapq.heappush(heap, (grid[r][c-1], r, c-1))
            if r+1 < rows and (r+1, c) not in visited:
                visited.add((r+1, c))
                heapq.heappush(heap, (grid[r+1][c], r+1, c))
            if c+1 < cols and (r, c+1) not in visited:
                visited.add((r, c+1))
                heapq.heappush(heap, (grid[r][c+1], r, c+1))
