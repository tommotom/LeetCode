class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        mod = 10**9 + 7
        tell = [0] * (n+1)
        know = [0] * (n+1)
        know[1] = 1
        for day in range(2, n+1):
            tell[day] = tell[day-1] - know[day-forget] + know[day-delay]
            tell[day] %= mod
            know[day] = tell[day]

        return (tell[-1] + sum(know[n-delay+1:])) % mod
