class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        if len(A) < 3: return 0

        diffs = []
        for i in range(len(A)-1):
            diffs.append(A[i+1] - A[i])

        idx, diff = 0, diffs[0]
        ans = 0
        for i in range(1, len(diffs)):
            if diff != diffs[i]:
                idx = i
                diff = diffs[i]
            ans += i - idx

        return ans
