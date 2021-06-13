class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        covered = [False for _ in range(right - left + 1)]
        for s, e in ranges:
            for num in range(max(s,left), min(e,right)+1):
                covered[num-left] = True
        return all(covered)
