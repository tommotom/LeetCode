class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        def isOverlap(int1, int2):
            return int1[0] <= int2[0] <= int1[1]

        ans = []
        for interval in intervals:
            if ans and isOverlap(ans[-1], interval):
                ans[-1][1] = max(ans[-1][1], interval[1])
            else:
                ans.append(interval)

        return ans
