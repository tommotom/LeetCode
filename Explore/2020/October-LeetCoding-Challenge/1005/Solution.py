class Solution:
    def bitwiseComplement(self, N: int) -> int:
        return int('1' * len(format(N, 'b')), 2) ^ N
