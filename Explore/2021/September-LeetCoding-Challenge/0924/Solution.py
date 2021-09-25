class Solution:
    def tribonacci(self, n: int) -> int:
        tribonacci = [0, 1, 1]
        for i in range(3, 38):
            sum = tribonacci[i-1] + tribonacci[i-2] + tribonacci[i-3]
            tribonacci.append(sum)

        return tribonacci[n]
