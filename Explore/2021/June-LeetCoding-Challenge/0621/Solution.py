class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def comb(n, r):
            return math.factorial(n) // (math.factorial(n-r) * math.factorial(r))
        return [[comb(num, n) for n in range(num+1)] for num in range(numRows)]
