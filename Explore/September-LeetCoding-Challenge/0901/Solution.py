class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        def isValid(A):
            h = A[0] * 10 + A[1]
            m = A[2] * 10 + A[3]
            return 0 <= h <= 23 and 0 <= m <= 59

        A.sort(reverse=True)

        for i in range(4):
            for j in range(4):
                if i == j: continue
                for k in range(4):
                    if i == k or j == k: continue
                    l = 6 - i - j - k
                    if isValid((A[i], A[j], A[k], A[l])):
                        return str(A[i]) + str(A[j]) + ":" + str(A[k]) + str(A[l])
        return ""
