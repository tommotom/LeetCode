class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        prime = [True for i in range(right+1)]
        prime[0] = False
        prime[1] = False

        sqrt_n = math.ceil(math.sqrt(right))
        for i in range(2, sqrt_n+1):
            if prime[i]:
                for j in range(2*i, right+1, i):
                    prime[j] = False

        i = left
        while i < len(prime) and not prime[i]:
            i += 1

        j = i + 1
        while j < len(prime) and not prime[j]:
            j += 1

        if j >= len(prime) or not prime[j]:
            return [-1, -1]

        ans = [i, j]
        while j < len(prime):
            i = j
            j += 1
            while j < len(prime) and not prime[j]:
                j += 1
            if j < len(prime) and prime[j]:
                if ans[1] - ans[0] > j - i:
                    ans = [i, j]

        return ans
