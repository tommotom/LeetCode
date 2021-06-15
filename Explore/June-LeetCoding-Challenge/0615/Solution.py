class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        s = sum(matchsticks)
        if not s % 4 == 0: return False

        l = s // 4
        n = len(matchsticks)
        matchsticks.sort(reverse=True)
        used = [False for _ in range(n)]
        def canMake(matchsticks, n, used, l):
            if l == 0: return used
            for i in range(n):
                if not used[i] and matchsticks[i] <= l:
                    used[i] = True
                    if canMake(matchsticks, n, used, l-matchsticks[i]):
                        return used
                    used[i] = False
            return False

        def helper(matchsticks, n, used, l, rest):
            if all(used) and rest == 0: return True
            if all(used) or rest == 0: return False

            idx = -1
            for i in range(n):
                if not used[i]:
                    used[i] = True
                    idx = i
                    break

            if matchsticks[idx] > l: return False
            if matchsticks[idx] == l:
                used[idx] = True
                return helper(matchsticks, n, used, l, rest-1)

            used = canMake(matchsticks, n, used, l-matchsticks[idx])
            if not used: return False
            else: return helper(matchsticks, n, used, l, rest-1)

        return helper(matchsticks, n, used, l, 4)
