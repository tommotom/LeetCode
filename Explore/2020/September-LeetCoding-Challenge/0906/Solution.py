class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:

        ans = 0
        for i in range(len(B)-1):
            for j in range(len(B[0])-1):
                tmp = [[b for b in row[j:]] for row in B[i:]]
                ans = max(self.countOverlap(A, tmp), ans)

        for i in range(len(A)-1):
            for j in range(len(A[0])-1):
                tmp = [[a for a in row[j:]] for row in A[i:]]
                ans = max(self.countOverlap(B, tmp), ans)

        return ans

    def countOverlap(self, A, B):
        rows = min(len(A), len(B))
        cols = min(len(A[0]), len(B[0]))

        count = 0
        for i in range(rows):
            for j in range(cols):
                if A[i][j] == 1 and B[i][j] == 1:
                    count += 1

        return count
