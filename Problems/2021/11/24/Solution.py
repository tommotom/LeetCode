class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        ans = []
        i = j = 0
        while i < len(A) and j < len(B):
            start_a, end_a = A[i]
            start_b, end_b = B[j]

            if start_a <= start_b <= end_a:
                ans.append([start_b, min(end_a, end_b)])
            elif start_a <= end_b <= end_a:
                ans.append([max(start_a, start_b), end_b])
            elif start_b <= start_a <= end_b:
                ans.append([start_a, min(end_a, end_b)])
            elif start_b <= end_a <= end_b:
                ans.appned([max(start_a, start_b), end_a])

            if end_a <= end_b:
                i += 1
            else:
                j += 1

        return ans
