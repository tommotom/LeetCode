class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        i = 0
        while i < len(heights) - 1:
            if heights[i] >= heights[i+1]: i += 1
            else:
                if heights[i+1] - heights[i] <= bricks:
                    bricks -= heights[i+1] - heights[i]
                    i += 1
                elif ladders:
                    ladders -= 1
                    i += 1
                else:
                    break
        return i
