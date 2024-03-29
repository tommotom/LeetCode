class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        prime = [True for i in range(n+1)]
        prime[0] = False
        prime[1] = False

        sqrt_n = math.ceil(math.sqrt(n))
        for i in range(2, sqrt_n):
            if prime[i]:
                for j in range(2*i, n+1, i):
                    prime[j] = False

        ans = []
        for x in range(1, n//2+1):
            if not prime[x]: continue
            y = n - x
            if x > y: break
            if not prime[y]: continue
            ans.append([x, y])

        return ans
