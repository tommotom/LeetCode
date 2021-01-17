class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        maxLen = count = 0
        for rectangle in rectangles:
            if maxLen < min(rectangle):
                maxLen = min(rectangle)
                count = 0
            if maxLen == min(rectangle): count += 1

        return count
