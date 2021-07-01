class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        for i in range(len(A)-1):
            if A[i] > i and (A[i] != i+1 or A[i+1] != i): return False
        return True
