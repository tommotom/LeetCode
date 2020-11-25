class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        visited = set()
        modulo = ans = 1
        while modulo:
            if modulo // K > 0:
                if modulo in visited: return -1
                visited.add(modulo)
                modulo %= K
                if modulo == 0: return ans
            modulo = modulo * 10 + 1
            ans += 1
        return ans
