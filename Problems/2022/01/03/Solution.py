class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted_by = [[] for _ in range(n+1)]
        trusts_someone = [False for _ in range(n+1)]

        for a, b in trust:
            trusted_by[b].append(a)
            trusts_someone[a] = True

        for i in range(1, n+1):
            if len(trusted_by[i]) == n-1 and not trusts_someone[i]: return i

        return -1
