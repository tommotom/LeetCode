class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        ratio_count = defaultdict(int)
        for x, y in rectangles:
            ratio_count[x/y] += 1
        ans = 0
        for count in ratio_count.values():
            ans += (count * (count - 1)) // 2
        return ans
