class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        b = []
        total = 0
        for i in range(1, len(heights)):
            diff = heights[i] - heights[i-1]
            if diff <= 0: continue
            heapq.heappush(b, diff)
            while len(b) > ladders:
                total += heapq.heappop(b)
            if total > bricks: return i - 1
        return len(heights) - 1
