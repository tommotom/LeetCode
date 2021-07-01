class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights: return 0
        length = len(heights)
        if length == 1: return heights[0]

        lptr = length//2 - 1
        rptr = length//2

        left = self.largestRectangleArea(heights[:rptr])
        right = self.largestRectangleArea(heights[rptr:])

        height = min(heights[lptr], heights[rptr])
        mid = height * (rptr - lptr + 1)
        while lptr > 0 and rptr + 1 < length:
            if heights[lptr-1] > heights[rptr+1]:
                lptr -= 1
                height = min(height, heights[lptr])
                mid = max(mid, height * (rptr - lptr + 1))
            else:
                rptr += 1
                height = min(height, heights[rptr])
                mid = max(mid, height * (rptr - lptr + 1))

        while lptr > 0:
            lptr -= 1
            height = min(height, heights[lptr])
            mid = max(mid, height * (rptr - lptr + 1))

        while rptr + 1 < length:
            rptr += 1
            height = min(height, heights[rptr])
            mid = max(mid, height * (rptr - lptr + 1))

        return max(left, mid, right)
