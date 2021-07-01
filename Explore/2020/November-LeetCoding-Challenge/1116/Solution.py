class Solution:
    def longestMountain(self, A: List[int]) -> int:
        climbed = descended = ans = 0

        for i in range(1, len(A)):
            if A[i-1] < A[i]:
                if descended: climbed = 0
                climbed += 1
                descended = 0
            elif A[i-1] > A[i]:
                descended += 1
            else:
                climbed = descended = 0

            if climbed and descended: ans = max(ans, climbed + descended + 1)

        return ans
