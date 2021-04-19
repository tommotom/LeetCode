class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        bit1 = [0 for _ in range(32)]
        for num1 in arr1:
            for i in range(32):
                if 1 << i & num1: bit1[i] += 1

        bit2 = [0 for _ in range(32)]
        for num2 in arr2:
            for i in range(32):
                if 1 << i & num2: bit2[i] += 1

        ans = 0
        for i in range(32):
            if bit1[i] % 2 == 1 and bit2[i] % 2 == 1:
                ans += 1<<i

        return ans
