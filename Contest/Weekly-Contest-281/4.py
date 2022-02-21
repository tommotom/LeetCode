class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        divisors = []
        for i in range(1, k+1):
            if k % i == 0:
                divisors.append(i)

        ans = 0
        counter = Counter()
        for i in range(len(nums)):
            remainder = k // math.gcd(k, nums[i])
            ans += counter[remainder]
            for divisor in divisors:
                if nums[i] % divisor == 0:
                    counter[divisor] += 1

        return ans
