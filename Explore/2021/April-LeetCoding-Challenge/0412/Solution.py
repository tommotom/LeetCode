class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        return [i//2+1 if i % 2 == 0 else k+1-i//2 for i in range(k+1)] + [i for i in range(k+2, n+1)]
