class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        ans = []

        count, target = 0, A[0]
        for i in range(1, len(A)):
            if A[i] == target: continue
            if B[i] != target: break
            count += 1
        else:
            ans.append(count)

        count, target = 0, B[0]
        for i in range(1, len(A)):
            if B[i] == target: continue
            if A[i] != target: break
            count += 1
        else:
            ans.append(count)

        count, target = 1, A[0]
        for i in range(1, len(A)):
            if B[i] == target: continue
            if A[i] != target: break
            count += 1
        else:
            ans.append(count)

        count, target = 1, B[0]
        for i in range(1, len(A)):
            if A[i] == target: continue
            if B[i] != target: break
            count += 1
        else:
            ans.append(count)

        if not ans: return -1
        return min(ans)
