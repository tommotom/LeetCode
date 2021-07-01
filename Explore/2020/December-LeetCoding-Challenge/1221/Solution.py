class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        A.sort()

        max_constant = A[-1] - K
        min_constant = A[0] + K

        ans = A[-1] - A[0]
        for i in range(len(A)-1):
            maximum = max(max_constant, A[i] + K)
            minimum = min(min_constant, A[i+1] - K)
            ans = min(ans, maximum - minimum)
        return ans
