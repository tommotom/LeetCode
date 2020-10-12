class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if not len(A) == len(B): return False
        duplicate = False
        passed = set()
        a = b = -1
        for i in range(len(A)):
            if A[i] != B[i]:
                if a < 0:
                    a = i
                elif b < 0:
                    b = i
                else: return False
            if A[i] in passed:
                duplicate = True
            passed.add(A[i])

        if a < 0 and b < 0: return duplicate
        if b < 0: return False

        return A[a] == B[b] and A[b] == B[a]
