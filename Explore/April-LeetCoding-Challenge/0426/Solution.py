class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        idx, ladder = 0, []
        while idx < len(heights) - 1:
            diff = heights[idx+1] - heights[idx]
            if diff <= 0:
                idx += 1
                continue

            if len(ladder) < ladders:
                heapq.heappush(ladder, diff)
            elif ladder and diff > ladder[0]:
                bricks -= heapq.heappop(ladder)
                heapq.heappush(ladder, diff)
            else:
                bricks -= diff

            if bricks < 0: break
            idx += 1

        return idx
